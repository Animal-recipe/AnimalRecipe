from django.shortcuts import render
from django.core.paginator import Paginator
from question.models import Question, Answer
from recipe.models import Recipe_Img, Recipe
from review.models import Review, Review_Img
from django.db.models import Count

def home(request):
    if request.method == 'GET':
        hot_recipes = Recipe.objects.all().annotate(num_like=Count('like')).order_by('-num_like')
        img = Recipe_Img.objects.all()
        hot_recipes_dict = {}

        if hot_recipes.__len__() >= 4:
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

        best_review = Review.objects.all().annotate(num_like=Count('like')).order_by('-num_like')
        img2 = Review_Img.objects.all()
        best_review_dict = {}

        if best_review.__len__() >= 4:
            for i in range(0, best_review.__len__()):
                temp = best_review[i]
                img_obj = ""
                for j in range(0, img2.__len__()):
                    if img2[j].review == temp:
                        img_obj = img2[j]
                        break
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
                img_obj = ""
                for j in range(0, recipeImg.__len__()):
                    if recipeImg[j].recipe == tmp:
                        img_obj = recipeImg[j]
                        break
                if img_obj != "":
                    recipes_dict[recipes[i]] = img_obj.image.url
                else:
                    recipes_dict[recipes[i]] = ""
        if reviews.exists():
            reviewImg = Review_Img.objects.all()
            for i in range(0, reviews.__len__()):
                tmp = reviews[i]
                img_obj = ""
                for j in range(0, reviewImg.__len__()):
                    if reviewImg[j].review == tmp:
                        img_obj = reviewImg[j]
                        break
                if img_obj != "":
                    reviews_dict[reviews[i]] = img_obj.image.url
                else:
                    reviews_dict[reviews[i]] = ""
        return render(request, "home/homeSearchResult.html", {'questions': questions, 'q': q, "recipes_dict":recipes_dict, 'reviews_dict': reviews_dict})
    else:
        return render(request, "home/homeSearchResult.html")

def page_not_found(request, exception):
    """
    404 Page not found
    """
    return render(request, 'home/404.html', {})

def server_error_page(request):
    """
    500 Page not found
    """
    return render(request, 'home/500.html', {})
