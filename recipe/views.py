from django.shortcuts import render
from .models import Recipe_Img,Recipe_Step,Recipe_Ingredient,Recipe
from .forms import RecipeImageFormSet,RecipeIngredientFormSet,RecipeStepFormSet, RecipeForm
from django.db import transaction
from django.shortcuts import redirect
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator

# Create your views here.
def create(request):
    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST, request.FILES)
        image_formset = RecipeImageFormSet(request.POST, request.FILES)
        ingredient_formset = RecipeIngredientFormSet(request.POST, request.FILES)
        step_formset = RecipeStepFormSet(request.POST, request.FILES)
        if ingredient_formset.is_valid() and image_formset.is_valid() and step_formset.is_valid() :
            recipe = recipe_form.save(commit=False)
            recipe.author_id = request.user.id
            recipe.animal = request.POST["animal"]
            recipe.cooking_time = request.POST["cooking_time"]
            recipe.level = request.POST["level"]
            recipe.title = request.POST["title"]
            recipe.summary = request.POST["summary"]
            recipe.count = request.POST["count"]

            with transaction.atomic():
                recipe.save()
                image_formset.instance = recipe
                ingredient_formset.instance = recipe
                step_formset.instance = recipe
                image_formset.save()
                ingredient_formset.save()
                step_formset.save()
                return redirect('/')
    else:
        image_formset = RecipeImageFormSet()
        ingredient_formset = RecipeIngredientFormSet()
        step_formset = RecipeStepFormSet()

    return render(request, '../templates/recipe/recipe_create.html', {
        'image_formset': image_formset,
        'ingredient_formset': ingredient_formset,
        'step_formset': step_formset,
    })

def recipe_home(request):

    return render(request, "../templates/recipe/recipe_home.html")

def recipe_list(request):  # 카테고리, 지역에 따라 list가 다릅니다\
    recipes = Recipe.objects.all()
    img = Recipe_Img.objects.all()
    recipes_dict={}
    #recipe를 key로 하고, image url을 value로 하는 맵 생성
    paginator = Paginator(recipes, 12) #12개로 제한
    page = request.GET.get('page') #??
    recipes =paginator.get_page(page)

    for i in range(0, recipes.__len__()):
        tmp = recipes[i]
        for j in range(0, img.__len__()):
            if img[j].recipe == tmp:
                img_obj = img[j]
        recipes_dict[recipes[i]] = img_obj.image.url

    return render(request, "../templates/recipe/recipe_list.html",
                  {"recipes_dict": recipes_dict, "recipes": recipes})

def recipe_detail(request, recipe_id):  # 카테고리, 지역에 따라 list가 다릅니다\
    recipe = Recipe.objects.get(pk=recipe_id)
    img_list = Recipe_Img.objects.filter(recipe=recipe)
    ingredient_list = Recipe_Ingredient.objects.filter(recipe=recipe)
    step_list = Recipe_Step.objects.filter(recipe=recipe)

    return render(request, "../templates/recipe/recipe_detail.html",
                  {"recipe": recipe, "img_list": img_list, "ingredient_list": ingredient_list, "step_list": step_list})