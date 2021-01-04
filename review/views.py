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

def review_list(request):  # 카테고리, 지역에 따라 list가 다릅니다\
    review = Review.objects.all()
    img = Review_Img.objects.all()
    review_dict={}
    #recipe를 key로 하고, image url을 value로 하는 맵 생성
    paginator = Paginator(review, 12) #12개로 제한
    page = request.GET.get('page') #??
    reveiw =paginator.get_page(page)

    best_review = Review.objects.all().order_by('-like')
    best_review_dict = {}
    for i in range(0, 4):
        temp = best_review[i]
        for j in range(0, img.__len__()):
            if img[j].review == temp:
                img_obj = img[j]
        best_review_dict[temp] = img_obj.image.url

    for i in range(0, review.__len__()):
        tmp = review[i]
        for j in range(0, img.__len__()):
            if img[j].review == tmp:
                img_obj = img[j]
        review_dict[review[i]] = img_obj.image.url

    return render(request, "review/review_list.html",{"review_dict":review_dict, "best_review_dict":best_review_dict})

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

@login_required
def review_detail(request, review_id):  # 카테고리, 지역에 따라 list가 다릅니다\
    review = Review.objects.get(pk=review_id)
    img_list = Review_Img.objects.filter(review=review)
    received_list = Message.objects.filter(recipient=request.user)
    send_list = Message.objects.filter(sender=request.user)
    review.hits = review.hits + 1
    review.save()

    click_like = 0
    for temp in review.like.all():
        if temp == request.user:
            click_like = 1
            break

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
