from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Message, Remessage
from account.models import User
from .forms import MessageForm, RemessageForm


def sendMessage(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)

        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.recipient = User.objects.get(username=form.cleaned_data.get("recipient"))
            message.content = form.cleaned_data.get("content")
            message.save()
            return redirect('listMessage')

        else:
            return HttpResponse('해당하는 아이디가 존재하지 않습니다. 다시 확인해주세요.')

    else:
        form = MessageForm()
        return render(request, 'contact/sendMessage.html', {'form': form})

def listMessage(request):
    receivedList = Message.objects.filter(recipient=request.user)
    remessage = Remessage.objects.filter(recipient=request.user)
    sentList = Message.objects.filter(sender=request.user)
    resentList = Remessage.objects.filter(sender=request.user)

    return render(request, 'contact/listMessage.html', {'rlist': receivedList, 'slist': sentList, 'remessage': remessage, 'resentList': resentList})

def viewMessage(request, message_id):
    if not request.user.is_authenticated:
        return redirect('/')
    messages = get_object_or_404(Message, pk=message_id)
    remessage = Remessage.objects.filter(message=messages)
    if request.user == messages.recipient:
        messages.isRead = True
    messages.save()
    form = RemessageForm(request.POST)
    return render(request, 'contact/viewMessage.html', {'message': messages, 'form':form, 'remessage': remessage})

def test(request):
    return render(request, 'contact/test.html')

def create_remessage(request, message_id):
    if request.method == 'POST':
        form = RemessageForm(request.POST)
        if form.is_valid():
            re_message = form.save(commit=False)
            re_message.sender = request.user
            re_message.recipient = Message.objects.get(id=message_id).sender
            re_message.message = Message.objects.get(id=message_id)
            re_message.content = form.cleaned_data.get("content")
            re_message.save()
            return redirect('listMessage')
    else:
        form = RemessageForm()
        return render(request, 'contact/viewMessage.html', {'form': form})