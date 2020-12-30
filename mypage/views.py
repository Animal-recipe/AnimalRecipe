from django.shortcuts import render
from question.models import Question, Answer
from recipe.models import Recipe
from review.models import Review
from question.forms import QuestionForm
from django.shortcuts import redirect
from django.core.paginator import Paginator
# Create your views here.
def myQuestion(request):
    questions = Question.objects.all()
    myQuestions = questions.filter(author=request.user)
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
