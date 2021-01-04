from django.shortcuts import render
from question.models import Question, Answer
from recipe.models import Recipe_Img, Recipe
from review.models import Review, Review_Img
from question.forms import QuestionForm
from django.shortcuts import redirect
from django.core.paginator import Paginator
from account.forms import UserChangeForm

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

def saveRecipe(request):
    user = request.user
    # saveRecipes = user.like_recipe.all()
    saveRecipes = user.save_recipe.all()
    print(saveRecipes)
    img = Recipe_Img.objects.filter()
    recipes_dict={}
    for i in range(0, saveRecipes.__len__()):
        tmp = saveRecipes[i]
        for j in range(0, img.__len__()):
            if img[j].recipe == tmp:
                img_obj = img[j]
                recipes_dict[saveRecipes[i]] = img_obj.image.url
    recipes = tuple(recipes_dict.items())
    page = request.GET.get('page', 1)
    paginator = Paginator(recipes, 12)
    recipeList =paginator.get_page(page)
    return render(request, "mypage/saveRecipe.html",{"recipeList":recipeList})

def delete_saveRecipe(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    recipe.save_count.remove(request.user)
    return redirect('mypage:saveRecipe')

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

def detail_myInfo(request):
    userPassword = '*' * request.user.passwordLength
    return render(request, 'mypage/detail_myInfo.html',{"userPassword":userPassword})

def update_myInfo(request):
    if request.method == "POST":
        form = UserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('account:login')
    else:
        form = UserChangeForm(instance = request.user)
    return render(request, 'mypage/update_myInfo.html', {'form': form})
