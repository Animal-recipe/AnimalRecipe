from django.shortcuts import render
from .forms import QuestionForm, AnswerForm
from django.shortcuts import redirect
from .models import Question, Answer

# Create your views here.
def question_create(request):
    if request.method == 'POST':
        question_form = QuestionForm(request.POST, request.FILES)
        if question_form.is_valid():
            question = question_form.save(commit=False)
            question.author_id = request.user.id
            question.save()

            return redirect('list_question')
    else:
        question_form = QuestionForm()

    return render(request, '../templates/question/question_create.html', {
        'question_form': question_form,
    })

def answer_create(request, question_id):
    if request.method == 'POST':
        answer_form = AnswerForm(request.POST, request.FILES)
        if answer_form.is_valid():
            answer = answer_form.save(commit=False)
            answer.author_id = request.user.id
            answer.question = Question.objects.get(pk=question_id)
            answer.save()
            # 해당 질문에 대한 페이지로 이동하려면 어떻게?!
            return redirect('list_question')
    else:
        answer_form = AnswerForm()

    return render(request, '../templates/question/answer_create.html', {
        'answer_form': answer_form,
    })

def question_list(request):
    question = Question.objects.all()

    return render(request, "../templates/question/question_list.html", {"question":question})

def question_detail(request, question_id):  # 카테고리, 지역에 따라 list가 다릅니다\
    question = Question.objects.get(pk=question_id)
    answer = Answer.objects.filter(question=question)

    return render(request, "../templates/question/question_detail.html",
                  {"question": question, "answer": answer})