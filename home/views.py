from django.shortcuts import render
from django.core.paginator import Paginator
from question.models import Question, Answer
from recipe.models import Recipe_Img, Recipe
from review.models import Review, Review_Img
from django.shortcuts import redirect

def home(request):
    if request.method == 'GET':
        return render(request, 'home/home.html')
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
