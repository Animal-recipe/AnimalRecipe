from django.shortcuts import render
from .models import Review, Review_Img, Recipe
from .forms import ReviewForm, ReviewImageForm, ReviewImageFormSet
from django.db import transaction
from django.shortcuts import redirect
from django.core.paginator import Paginator

# Create your views here.
def review_list(request):  # 카테고리, 지역에 따라 list가 다릅니다\
    review = Review.objects.all()
    img = Review_Img.objects.all()
    review_dict={}
    #recipe를 key로 하고, image url을 value로 하는 맵 생성
    paginator = Paginator(review, 12) #12개로 제한
    page = request.GET.get('page') #??
    reveiw =paginator.get_page(page)

    for i in range(0, review.__len__()):
        tmp = review[i]
        for j in range(0, img.__len__()):
            if img[j].review == tmp:
                img_obj = img[j]
        review_dict[review[i]] = img_obj.image.url

    return render(request, "review/review_list.html",{"review_dict":review_dict})

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
                return redirect('/')
    else:
        image_formset = ReviewImageFormSet()

    return render(request, '../templates/review/review_create.html', {
        'image_formset': image_formset,
    })

def review_detail(request, review_id):  # 카테고리, 지역에 따라 list가 다릅니다\
    review = Review.objects.get(pk=review_id)
    img_list = Review_Img.objects.filter(review=review)

    return render(request, "review/review_detail.html",
                  {"review": review, "img_list": img_list})

def delete(request, review_id):
    review = Review.objects.get(pk=review_id)
    review.delete()
    return redirect('/')

def edit(request, review_id):
    now_review = Review.objects.get(pk=review_id)
    if now_review.author_id != request.user.id:
        return redirect('/')
    if request.method == 'POST':
        image_formset = ReviewImageFormSet(request.POST, request.FILES, instance=now_review)
        now_review.title = request.POST["title"]
        now_review.star = request.POST["star"]
        now_review.content = request.POST["content"]
        now_review.save()
        if image_formset.is_valid():
            image_formset.save()
            return redirect('/')
    else:
        image_formset = ReviewImageFormSet(instance=now_review)

    return render(request, '../templates/review/review_edit.html', {
        'image_formset': image_formset, 'now_review': now_review,
    })
