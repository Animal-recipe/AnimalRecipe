from django.shortcuts import render
from .forms import QuestionForm, AnswerForm
from django.shortcuts import redirect
from .models import Question, Answer

# Create your views here.
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            question = form.save(commit=False)
            question.author_id = request.user.id
            question.save()

            return redirect('/question/list/')
    else:
        form = QuestionForm()

    return render(request, '../templates/question/question_create.html', {
        'form': form,
    })

def answer_create(request, question_id):
    question = Question.objects.get(pk=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author_id = request.user.id
            answer.question = question
            answer.save()
            return redirect('question:detail', question_id=question_id)
    else:
        form = AnswerForm()

    return render(request, '../templates/question/answer_create.html', 
        {"form": form, "question": question}
    )

def question_list(request):
    question = Question.objects.all()

    return render(request, "../templates/question/question_list.html", {"question":question})

def question_detail(request, question_id):  # 카테고리, 지역에 따라 list가 다릅니다\
    question = Question.objects.get(pk=question_id)
    answer = Answer.objects.filter(question=question)

    return render(request, "../templates/question/question_detail.html",
                  {"question": question, "answer": answer})