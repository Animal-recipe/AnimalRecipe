from django.shortcuts import render
from question.models import Question, Answer
from recipe.models import Recipe_Img, Recipe
from review.models import Review, Review_Img
from question.forms import QuestionForm
from django.shortcuts import redirect
from django.core.paginator import Paginator

def myQuestion(request):
    myQuestions = Question.objects.filter(author=request.user)
    page = request.GET.get('page', 1)
    paginator = Paginator(myQuestions, 10)
    pageObject = paginator.get_page(page)
    return render(request, "mypage/myQuestion.html", {"questions":pageObject})

def delete_myQuestion(request, question_id):
    question = Question.objects.get(pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제 권한이 없습니다')
        return redirect('question:detail', question_id=question.id)
    else:
        question.delete()
    return redirect('mypage:myQuestion')

def myRecipe(request):
    myRecipes = Recipe.objects.filter(author=request.user)
    img = Recipe_Img.objects.filter()
    recipes_dict={}
    for i in range(0, myRecipes.__len__()):
        tmp = myRecipes[i]
        for j in range(0, img.__len__()):
            if img[j].recipe == tmp:
                img_obj = img[j]
        recipes_dict[myRecipes[i]] = img_obj.image.url
    recipes = tuple(recipes_dict.items())
    page = request.GET.get('page', 1)
    paginator = Paginator(recipes, 12)
    recipeList =paginator.get_page(page)
    return render(request, "mypage/myRecipe.html",{"recipeList":recipeList})

def delete_myRecipe(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    if recipe.author_id != request.user.id:
        return redirect('recipe:list_recipe')
    recipe.delete()
    return redirect('mypage:myRecipe')

def myReview(request):
    myReviews = Review.objects.filter(author=request.user)
    img = Review_Img.objects.all()
    review_dict={}
    for i in range(0, myReviews.__len__()):
        tmp = myReviews[i]
        for j in range(0, img.__len__()):
            if img[j].review == tmp:
                img_obj = img[j]
        review_dict[myReviews[i]] = img_obj.image.url
    reviews = tuple(review_dict.items())
    page = request.GET.get('page', 1)
    paginator = Paginator(reviews, 12)
    reviewList =paginator.get_page(page)
    return render(request, "mypage/myReview.html",{"reviewList":reviewList})

def delete_myReview(request, review_id):
    review = Review.objects.get(pk=review_id)
    if review.author_id != request.user.id:
        return redirect('review:list_review')
    review.delete()
    return redirect('mypage:myReview')
