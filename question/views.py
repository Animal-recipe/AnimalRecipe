from django.shortcuts import render
from .forms import QuestionForm, AnswerForm
from django.shortcuts import redirect
from .models import Question, Answer
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from contact.models import Message
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import View
from django.http import HttpResponseForbidden
from django.http import HttpResponseRedirect
from urllib.parse import urlparse
from django.shortcuts import resolve_url

@login_required
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            question = form.save(commit=False)
            question.author_id = request.user.id
            question.save()
            return redirect('/question/list/')
        else:
            pass
    else:
        form = QuestionForm()
    return render(request, 'question/createQuestion.html', {'form': form,})

@login_required
def update_question(request, question_id):
    question = Question.objects.get(pk=question_id)
    if request.user != question.author:
        messages.error(request, '수정 권한이 없습니다')
        return redirect('question:detail', question_id=question.id)
    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            return redirect('question:detail', question_id=question.id)
    else:
        form = QuestionForm(instance=question)
    return render(request, 'question/createQuestion.html', {'form': form})

@login_required
def delete_question(request, question_id):
    question = Question.objects.get(pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제 권한이 없습니다')
        return redirect('question:detail', question_id=question.id)
    else:
        question.delete()
    return redirect('question:list')

@login_required
def create_answer(request, question_id):
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
            pass
    else:
        form = AnswerForm()
    return render(request, 'question/createAnswer.html', {"form": form, "question": question})

@login_required
def update_answer(request, answer_id):
    answer = Answer.objects.get(pk=answer_id)
    question = answer.question
    if request.user != answer.author:
        messages.error(request, '수정 권한이 없습니다')
        return redirect('question:detail', question_id=question.id)
    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.question = question
            answer.save()
            return redirect('question:detail', question_id=question.id)
    else:
        form = AnswerForm(instance=answer)
    return render(request, 'question/createAnswer.html', {'form': form, 'question': question})

@login_required
def delete_answer(request, answer_id):
    answer = Answer.objects.get(pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '삭제 권한이 없습니다')
        return redirect('question:detail', question_id=answer.question.id)
    elif answer.accept == True:
        messages.error(request, '채택된 답변은 삭제가 불가능합니다.')
        return redirect('question:detail', question_id=answer.question.id)
    else:
        answer.delete()
    return redirect('question:detail', question_id=answer.question.id)

def question_list(request):
    q = request.GET.get('q', "")
    page = request.GET.get('page', 1)
    if q:
        questions = Question.objects.filter(title__icontains=q, is_active=True)
    else:
        questions = Question.objects.all()
    paginator = Paginator(questions, 10)
    pageObject = paginator.get_page(page)
    return render(request, "question/listQuestion.html", {"questions":pageObject, "page":page, "q":q})

def question_detail(request, question_id):
    question = Question.objects.get(pk=question_id)
    answers = Answer.objects.filter(question=question, is_active=True).order_by('-accept')

    if request.user.is_anonymous:
        received_list = {}
        send_list = {}
    else:
        received_list = Message.objects.filter(recipient=request.user)
        send_list = Message.objects.filter(sender=request.user)

    return render(request, "../templates/question/detailQuestion.html", {"received_list": received_list, "send_list": send_list, "question": question, "answers": answers})

@login_required
def accept(request, answer_id):
    answerQuery = Answer.objects.filter(pk=answer_id)
    answer = Answer.objects.get(pk=answer_id)
    questionQuery = Question.objects.filter(pk=answer.question.id)
    question = Question.objects.get(pk=answer.question.id)
    if request.user != question.author:
        messages.error(request, '질문 작성자만 채택할 수 있습니다.')
    elif question.accept_done:
        messages.error(request, '이미 답변 채택이 완료되었습니다.')
    else:
        answerQuery.update(accept=True)
        questionQuery.update(accept_done=True)
    return redirect('{}#accept_btn_{}'.format(
        resolve_url('question:detail', question_id=question.id), answer_id
    ))

class answer_like(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:  # 로그인이 되어있지 않을 경우
            return HttpResponseForbidden()  # 아무일도 일어나지 않는다
        else:
            if 'answer_id' in kwargs:
                answer_id = kwargs['answer_id']
                answer = Answer.objects.get(pk=answer_id)
                user = request.user
                if user in answer.like.all():
                    answer.like.remove(user)
                else:
                    answer.like.add(user)

            referer_url = request.META.get('HTTP_REFERER')  # 성공했을 때 url을 옮기지 않고
            path = urlparse(referer_url).path+"#like_btn_"+str(answer_id)
            return HttpResponseRedirect(path)
