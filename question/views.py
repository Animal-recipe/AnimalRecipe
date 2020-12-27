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
            print('not valid form')
    else:
        form = QuestionForm()

    return render(request, 'question/createQuestion.html', {
        'form': form,
    })
def update_question(request, question_id):
    question = Question.objects.get(pk=question_id)
    if request.user != question.author:
        messages.error(request, '댓글수정권한이 없습니다')
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
    context = {'form': form}
    return render(request, 'question/createQuestion.html', context)

def delete_question(request, question_id):
    question = Question.objects.get(pk=question_id)
    if request.user != question.author:
        messages.error(request, '댓글 삭제권한이 없습니다')
        return redirect('question:detail', question_id=question.id)
    else:
        question.delete()
    return redirect('question:list')

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
            print('not valid')
    else:
        form = AnswerForm()
    return render(request, 'question/createAnswer.html', 
        {"form": form, "question": question}
    )
def update_answer(request, answer_id):
    print(answer_id)
    answer = Answer.objects.get(pk=answer_id)
    print(answer)
    print('up is answer')
    question = answer.question
    print(question)
    print('up is question.')
    if request.user != answer.author:
        messages.error(request, '댓글수정권한이 없습니다')
        return redirect('question:detail', question_id=answer.question.id)

    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.question = question
            answer.save()
            return redirect('question:detail', question_id=answer.question.id)
    else:
        form = AnswerForm(instance=answer)
    context = {'form': form, 'question': question}
    return render(request, 'question/createAnswer.html', context)
def delete_answer(request, answer_id):
    answer = Answer.objects.get(pk=answer_id)
    # question = answer.question
    if request.user != answer.author:
        messages.error(request, '댓글 삭제권한이 없습니다')
        return redirect('question:detail', question_id=answer.question.id)
    else:
        answer.delete()
    return redirect('question:detail', question_id=answer.question.id)
def question_list(request):
    questions = Question.objects.all()
    return render(request, "question/listQuestion.html", {"questions":questions})

def question_detail(request, question_id):  # 카테고리, 지역에 따라 list가 다릅니다\
    question = Question.objects.get(pk=question_id)
    answers = Answer.objects.filter(question=question).order_by('created')

    return render(request, "../templates/question/detailQuestion.html",
                  {"question": question, "answers": answers})
def search(request):
    questions = Question.objects.all().order_by('-created')
    q = request.POST.get('q', "")
    if q:
        questions = questions.filter(title__icontains=q)
        return render(request, "question/searchResult.html", {'questions': questions, 'q': q})
    else:
        return render(request, "question/searchResult.html")
