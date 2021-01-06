from django.shortcuts import render
from django.core.paginator import Paginator
from question.models import Question, Answer
from recipe.models import Recipe_Img, Recipe
from review.models import Review, Review_Img


def home(request):
    if request.method == 'GET':
        hot_recipes = Recipe.objects.all().order_by('-like')
        img = Recipe_Img.objects.all()
        hot_recipes_dict = {}

        if hot_recipes.__len__() >= 4:
            for i in range(0, 4):
                temp = hot_recipes[i]
                img_obj = ""
                for j in range(0, img.__len__()):
                    if img[j].recipe == temp:
                        img_obj = img[j]
                if img_obj != "":
                    hot_recipes_dict[temp] = img_obj.image.url
                else:
                    hot_recipes_dict[temp] = ""

        best_review = Review.objects.all().order_by('-like')
        img2 = Review_Img.objects.all()
        best_review_dict = {}

        if best_review.__len__() >= 4:
            for i in range(0, 4):
                temp = best_review[i]
                img_obj = ""
                for j in range(0, img2.__len__()):
                    if img2[j].review == temp:
                        img_obj = img2[j]
                if img_obj != "":
                    best_review_dict[temp] = img_obj.image.url
                else:
                    best_review_dict[temp] = ""

        return render(request, 'home/home.html', {"hot_recipes_dict": hot_recipes_dict, "best_review_dict":best_review_dict})

def search(request):
    q = request.POST.get('q', "")
    recipes_dict={}
    reviews_dict={}
    if q:
        questions = Question.objects.filter(title__icontains=q, is_active=True)
        recipes = Recipe.objects.filter(title__icontains=q)
        reviews = Review.objects.filter(title__icontains=q)
        if recipes.exists():
            recipeImg = Recipe_Img.objects.all()
            for i in range(0, recipes.__len__()):
                tmp = recipes[i]
                for j in range(0, recipeImg.__len__()):
                    if recipeImg[j].recipe == tmp:
                        img_obj = recipeImg[j]
                        recipes_dict[recipes[i]] = img_obj.image.url
        if reviews.exists():
            reviewImg = Review_Img.objects.all()
            for i in range(0, reviews.__len__()):
                tmp = reviews[i]
                for j in range(0, reviewImg.__len__()):
                    if reviewImg[j].review == tmp:
                        img_obj = reviewImg[j]
                        reviews_dict[reviews[i]] = img_obj.image.url
        return render(request, "home/homeSearchResult.html", {'questions': questions, 'q': q, "recipes_dict":recipes_dict, 'reviews_dict': reviews_dict})
    else:
        return render(request, "home/homeSearchResult.html")
