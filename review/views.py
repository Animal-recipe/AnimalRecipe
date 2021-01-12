from django.shortcuts import render
from .models import Review, Review_Img, Recipe
from .forms import ReviewForm, ReviewImageForm, ReviewImageFormSet
from django.db import transaction
from django.shortcuts import redirect
from django.core.paginator import Paginator
from contact.models import Message
from django.views.generic.base import View
from django.http import HttpResponseForbidden
from django.http import HttpResponseRedirect
from urllib.parse import urlparse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q, Count


def review_list(request):
    q= request.GET.get('q', "")
    page = request.GET.get('page', 1)
    petkind = request.GET.get('petkind', 'all')
    cooking_time = request.GET.get('cooking_time', 'all')
    order = request.GET.get('order', 'recent')

    img = Review_Img.objects.all()
    recipe = Recipe.objects.all()
    review_dict={}
    best_review = Review.objects.all().order_by('-like')
    best_review_dict = {}

    if best_review.__len__() >= 4:
        for i in range(0, 4):
            temp = best_review[i]
            img_obj = ""
            for j in range(0, img.__len__()):
                if img[j].review == temp:
                    img_obj = img[j]
                    break
            if img_obj != "":
                best_review_dict[temp] = img_obj.image.url
            else:
                best_review_dict[temp] = ""

    # 필터
    if petkind == 'dog':
        recipe = recipe.filter(Q(animal='강아지')|Q(animal='모두'))
    elif petkind == 'cat':
        recipe = recipe.filter(Q(animal='고양이')|Q(animal='모두'))
    elif petkind == 'etc':
        recipe = recipe.exclude(animal='강아지').exclude(animal='고양이')
    else:
        pass

    if cooking_time == 'under5':
        recipe = recipe.filter(cooking_time='5분이내')
    elif cooking_time == 'fiveTo10':
        recipe = recipe.filter(cooking_time='5분_10분')
    elif cooking_time == 'tenTo20':
        recipe = recipe.filter(cooking_time='10분_20분')
    elif cooking_time == 'over20':
        recipe = recipe.filter(cooking_time='20분이상')
    else:
        pass

    review = Review.objects.filter(recipe__in=recipe)

    # 검색
    if q:
        review = review.filter(title__icontains=q)
    else:
        pass

    # 순서
    if order == 'recent':
        review = review.order_by('-created')
    else:
        review = review.annotate(num_like=Count('like')).order_by('-num_like','-created')

    for i in range(0, review.__len__()):
        tmp = review[i]
        img_obj = ""
        for j in range(0, img.__len__()):
            if img[j].review == tmp:
                img_obj = img[j]
                break
        if img_obj != "":
            review_dict[review[i]] = img_obj.image.url
        else:
            review_dict[review[i]] = ""

    reviews = tuple(review_dict.items())
    paginator = Paginator(reviews, 12)
    reviews =paginator.get_page(page)
    context = {"reviews": reviews, "best_review_dict": best_review_dict, 'page': page, 'q': q, 'petkind': petkind, 'cooking_time': cooking_time, 'order': order}
    return render(request, "review/review_list.html", context)

@login_required
def create(request, recipe_id):
    if request.method == 'POST':
        review_form = ReviewForm(request.POST, request.FILES)
        image_formset = ReviewImageFormSet(request.POST, request.FILES)

        if image_formset.is_valid():
            review = review_form.save(commit=False)
            review.author_id = request.user.id
            review.recipe = Recipe.objects.get(pk=recipe_id)
            review.title = request.POST["title"]
            review.star = request.POST["star"]
            review.content = request.POST["content"]

            with transaction.atomic():
                review.save()
                review.save()
                image_formset.instance = review
                image_formset.save()
                return redirect('/review/list')
    else:
        image_formset = ReviewImageFormSet()

    return render(request, '../templates/review/review_create.html', {
        'image_formset': image_formset,
    })

def review_detail(request, review_id):  # 카테고리, 지역에 따라 list가 다릅니다\
    review = Review.objects.get(pk=review_id)
    img_list = Review_Img.objects.filter(review=review)
    if request.user.is_anonymous:
        received_list = {}
        send_list = {}
    else:
        received_list = Message.objects.filter(recipient=request.user)
        send_list = Message.objects.filter(sender=request.user)

    click_like = 0
    if not request.user.is_anonymous:
        for temp in review.like.all():
            if temp == request.user:
                click_like = 1
                break
    review.hits = review.hits + 1
    review.save()

    return render(request, "review/review_detail.html",
                  {"review": review, "img_list": img_list, 'received_list':received_list, 'send_list':send_list, 'click_like':click_like})

@login_required
def delete(request, review_id):
    review = Review.objects.get(pk=review_id)
    if review.author_id != request.user.id:
        return redirect('/review/list')
    review.delete()
    return redirect('/review/list')

@login_required
def edit(request, review_id):
    now_review = Review.objects.get(pk=review_id)
    if now_review.author_id != request.user.id:
        return redirect('/review/list')
    if request.method == 'POST':
        image_formset = ReviewImageFormSet(request.POST, request.FILES, instance=now_review)
        now_review.title = request.POST["title"]
        now_review.star = request.POST["star"]
        now_review.content = request.POST["content"]
        now_review.save()
        if image_formset.is_valid():
            image_formset.save()
            return redirect('/review/list')
    else:
        image_formset = ReviewImageFormSet(instance=now_review)

    return render(request, '../templates/review/review_edit.html', {
        'image_formset': image_formset, 'now_review': now_review,
    })

class Review_Like(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:  # 로그인이 되어있지 않을 경우
            return HttpResponseForbidden()  # 아무일도 일어나지 않는다
        else:
            if 'review_id' in kwargs:
                review_id = kwargs['review_id']
                review = Review.objects.get(pk=review_id)
                user = request.user
                if user in review.like.all():
                    review.like.remove(user)
                else:
                    review.like.add(user)

            referer_url = request.META.get('HTTP_REFERER')  # 성공했을 때 url을 옮기지 않고
            path = urlparse(referer_url).path
            return HttpResponseRedirect(path)