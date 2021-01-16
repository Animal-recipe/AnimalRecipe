from django.shortcuts import render
from .models import Recipe_Img,Recipe_Step,Recipe_Ingredient,Recipe
from .forms import RecipeImageFormSet,RecipeIngredientFormSet,RecipeStepFormSet, RecipeForm
from django.db import transaction
from django.shortcuts import redirect
from django.views.generic.edit import FormMixin
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator
from django.views.generic.base import View
from django.http import HttpResponseForbidden
from django.http import HttpResponseRedirect
from urllib.parse import urlparse
from django.db.models import Count
from review.models import Review, Review_Img
from contact.models import Message
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

@login_required
def create(request):
    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST, request.FILES)
        image_formset = RecipeImageFormSet(request.POST, request.FILES)
        ingredient_formset = RecipeIngredientFormSet(request.POST, request.FILES)
        step_formset = RecipeStepFormSet(request.POST, request.FILES)
        if ingredient_formset.is_valid() and image_formset.is_valid() and step_formset.is_valid() :
            recipe = recipe_form.save(commit=False)
            recipe.author_id = request.user.id
            if request.POST["animal"] == "기타":
                recipe.animal = request.POST["other"]
            else:
                recipe.animal = request.POST["animal"]

            recipe.cooking_time = request.POST["cooking_time"]
            recipe.level = request.POST["level"]
            recipe.title = request.POST["title"]
            recipe.summary = request.POST["summary"]

            with transaction.atomic():
                recipe.save()
                image_formset.instance = recipe
                ingredient_formset.instance = recipe
                step_formset.instance = recipe
                image_formset.save()
                ingredient_formset.save()
                step_formset.save()
                return redirect('/recipe/list')
    else:
        image_formset = RecipeImageFormSet()
        ingredient_formset = RecipeIngredientFormSet()
        step_formset = RecipeStepFormSet()

    return render(request, '../templates/recipe/recipe_create.html', {
        'image_formset': image_formset,
        'ingredient_formset': ingredient_formset,
        'step_formset': step_formset,
    })


def recipe_list(request):  # 카테고리, 지역에 따라 list가 다릅니다\
    q = request.GET.get('q', "")
    page = request.GET.get('page', 1)
    petkind = request.GET.get('petkind', 'all')
    cooking_time = request.GET.get('cooking_time', 'all')
    order = request.GET.get('order', 'recent')
    img = Recipe_Img.objects.all()
    recipes_dict={}
    hot_recipes = Recipe.objects.all().annotate(num_like=Count('like')).order_by('-num_like')
    hot_recipes_dict={}
    
    # 검색
    if q:
        recipes = Recipe.objects.filter(title__icontains=q)
    else:
        recipes =Recipe.objects.all()
    
    # 필터
    if petkind == 'dog':
        recipes = recipes.filter(Q(animal='강아지')|Q(animal='모두'))
    elif petkind == 'cat':
        recipes = recipes.filter(Q(animal='고양이')|Q(animal='모두'))
    elif petkind == 'etc':
        recipes = recipes.exclude(animal='강아지').exclude(animal='고양이')
    else:
        pass

    if cooking_time == 'under5':
        recipes = recipes.filter(cooking_time='5분이내')
    elif cooking_time == 'fiveTo10':
        recipes = recipes.filter(cooking_time='5분_10분')
    elif cooking_time == 'tenTo20':
        recipes = recipes.filter(cooking_time='10분_20분')
    elif cooking_time == 'over20':
        recipes = recipes.filter(cooking_time='20분이상')
    else:
        pass

    if order == 'recent':
        recipes = recipes.order_by('-created')
    elif order == 'review':
        recipes = recipes.annotate(num_review=Count('recipe_review')).order_by('-num_review', '-created')
    else:  # like
        recipes = recipes.annotate(num_like=Count('like')).order_by('-num_like','-created')

    if hot_recipes.__len__() >= 4 :
        for i in range(0, hot_recipes.__len__()):
            temp = hot_recipes[i]
            img_obj = ""
            for j in range(0, img.__len__()):
                if img[j].recipe == temp:
                    img_obj = img[j]
                    break
            if img_obj != "":
                hot_recipes_dict[temp] = img_obj.image.url
            else:
                hot_recipes_dict[temp] = ""

    for i in range(0, recipes.__len__()):
        tmp = recipes[i]
        img_obj = ""
        for j in range(0, img.__len__()):
            if img[j].recipe == tmp:
                img_obj = img[j]
                break
        if img_obj != "":
            recipes_dict[recipes[i]] = img_obj.image.url
        else:
            recipes_dict[recipes[i]] = ""

    recipes = tuple(recipes_dict.items())
    paginator = Paginator(recipes, 12)
    recipes = paginator.get_page(page)
    context = {"recipes": recipes, "hot_recipes_dict": hot_recipes_dict, 'page':page, 'q': q, 'petkind': petkind, 'cooking_time': cooking_time, 'order': order}
    return render(request, "recipe/recipe_list.html", context)

def recipe_detail(request, recipe_id):  # 카테고리, 지역에 따라 list가 다릅니다\
    recipe = Recipe.objects.get(pk=recipe_id)
    img_list = Recipe_Img.objects.filter(recipe=recipe)
    ingredient_list = Recipe_Ingredient.objects.filter(recipe=recipe)
    step_list = Recipe_Step.objects.filter(recipe=recipe)

    reviews = Review.objects.filter(recipe=recipe_id)
    review_img = Review_Img.objects.all()
    review_dict = {}
    count = 0

    for i in range(0, reviews.__len__()):
        tmp = reviews[i]
        count = count + 1
        img_obj = ""
        for j in range(0, review_img.__len__()):
            if review_img[j].review == tmp:
                img_obj = review_img[j]
                break
        if img_obj != "":
            review_dict[reviews[i]] = img_obj.image.url
        else:
            review_dict[reviews[i]] = ""
    reviews = tuple(review_dict.items())
    page = request.GET.get('page', 1)
    paginator = Paginator(reviews, 4)
    reviews =paginator.get_page(page)

    if request.user.is_anonymous:
        received_list = {}
        send_list = {}
    else:
        received_list = Message.objects.filter(recipient=request.user)
        send_list = Message.objects.filter(sender=request.user)

    click_like = 0
    if not request.user.is_anonymous:
        for temp in recipe.like.all():
            if temp == request.user:
                click_like = 1
                break

    click_save = 0
    if not request.user.is_anonymous:
        for temp in recipe.bookmark.all():
            if temp == request.user:
                click_save = 1
                break

    recipe.hits = recipe.hits + 1
    recipe.save()

    return render(request, "recipe/recipe_detail.html",
                  {"click_save": click_save, "received_list": received_list, "send_list": send_list, "recipe": recipe, "img_list": img_list, "ingredient_list": ingredient_list, "step_list": step_list, "reviews": reviews, "count":count, "click_like":click_like})

@login_required
def delete(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    if recipe.author_id != request.user.id:
        return redirect('/recipe/list')
    recipe.delete()
    return redirect('/recipe/list')

@login_required
def edit(request, recipe_id):
    now_recipe = Recipe.objects.get(pk=recipe_id)
    step_list = Recipe_Step.objects.filter(recipe=now_recipe)
    step_size = step_list.__len__()

    if now_recipe.author_id != request.user.id:
        return redirect('/recipe/list')
    if request.method == 'POST':
        image_formset = RecipeImageFormSet(request.POST, request.FILES, instance=now_recipe)
        ingredient_formset = RecipeIngredientFormSet(request.POST, request.FILES, instance=now_recipe)
        step_formset = RecipeStepFormSet(request.POST, request.FILES, instance=now_recipe)
        if request.POST["animal"] == "기타":
            now_recipe.animal = request.POST["other"]
        else:
            now_recipe.animal = request.POST["animal"]

        now_recipe.cooking_time = request.POST["cooking_time"]
        now_recipe.level = request.POST["level"]
        now_recipe.title = request.POST["title"]
        now_recipe.summary = request.POST["summary"]
        now_recipe.save()
        if ingredient_formset.is_valid() and image_formset.is_valid() and step_formset.is_valid() :
            with transaction.atomic():
                image_formset.instance = now_recipe
                ingredient_formset.instance = now_recipe
                step_formset.instance = now_recipe
                image_formset.save()
                ingredient_formset.save()
                step_formset.save()
                return redirect('/recipe/list')
    else:
        image_formset = RecipeImageFormSet(instance=now_recipe)
        ingredient_formset = RecipeIngredientFormSet(instance=now_recipe)
        step_formset = RecipeStepFormSet(instance=now_recipe)

    return render(request, '../templates/recipe/recipe_edit.html', {
        'image_formset': image_formset,
        'ingredient_formset': ingredient_formset,
        'step_formset': step_formset,
        'now_recipe': now_recipe,
        'step_size': step_size,
    })

class Recipe_Like(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:  # 로그인이 되어있지 않을 경우
            return HttpResponseForbidden()  # 아무일도 일어나지 않는다
        else:
            if 'recipe_id' in kwargs:
                recipe_id = kwargs['recipe_id']
                recipe = Recipe.objects.get(pk=recipe_id)
                user = request.user
                if user in recipe.like.all():
                    recipe.like.remove(user)
                else:
                    recipe.like.add(user)

            referer_url = request.META.get('HTTP_REFERER')  # 성공했을 때 url을 옮기지 않고
            path = urlparse(referer_url).path+"#like_btn"
            return HttpResponseRedirect(path)

class Recipe_Like2(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:  # 로그인이 되어있지 않을 경우
            return HttpResponseForbidden()  # 아무일도 일어나지 않는다
        else:
            if 'recipe_id' in kwargs:
                recipe_id = kwargs['recipe_id']
                recipe = Recipe.objects.get(pk=recipe_id)
                user = request.user
                if user in recipe.like.all():
                    recipe.like.remove(user)
                else:
                    recipe.like.add(user)

            referer_url = request.META.get('HTTP_REFERER')  # 성공했을 때 url을 옮기지 않고
            path = urlparse(referer_url).path+"#like_btn2"
            return HttpResponseRedirect(path)

class Recipe_Save(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:  # 로그인이 되어있지 않을 경우
            return HttpResponseForbidden()  # 아무일도 일어나지 않는다
        else:
            if 'recipe_id' in kwargs:
                recipe_id = kwargs['recipe_id']
                recipe = Recipe.objects.get(pk=recipe_id)
                user = request.user
                if user in recipe.bookmark.all():
                    recipe.bookmark.remove(user)
                else:
                    recipe.bookmark.add(user)

            referer_url = request.META.get('HTTP_REFERER')  # 성공했을 때 url을 옮기지 않고
            path = urlparse(referer_url).path+"#save_btn"
            return HttpResponseRedirect(path)

class Recipe_Save2(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:  # 로그인이 되어있지 않을 경우
            return HttpResponseForbidden()  # 아무일도 일어나지 않는다
        else:
            if 'recipe_id' in kwargs:
                recipe_id = kwargs['recipe_id']
                recipe = Recipe.objects.get(pk=recipe_id)
                user = request.user
                if user in recipe.bookmark.all():
                    recipe.bookmark.remove(user)
                else:
                    recipe.bookmark.add(user)

            referer_url = request.META.get('HTTP_REFERER')  # 성공했을 때 url을 옮기지 않고
            path = urlparse(referer_url).path+"#save_btn2"
            return HttpResponseRedirect(path)
