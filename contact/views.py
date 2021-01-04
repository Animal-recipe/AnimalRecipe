from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Message, Remessage
from account.models import User
from .forms import MessageForm, RemessageForm
from django.contrib.auth.decorators import login_required

@login_required
def contact_list(request):
    received_list = Message.objects.filter(recipient=request.user)
    send_list = Message.objects.filter(sender=request.user)
    return render(request, 'contact/contact_list.html', {'received_list': received_list, 'send_list': send_list })

@login_required
def contact_detail(request, contact_id):
    contact = Message.objects.get(pk=contact_id)
    return render(request, "contact/contact_detail.html", {"contact": contact})

@login_required
def contact_detail2(request, contact_id):
    contact = Message.objects.get(pk=contact_id)
    return render(request, "contact/contact_detail2.html", {"contact": contact})

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
            return redirect('/contact/list')
    else:
        form = RemessageForm()
        return render(request, 'contact/viewMessage.html', {'form': form})

def contact_create(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender_id = request.user.id
            message.recipient_id = User.objects.get(email=form.cleaned_data.get("recipient")).id
            message.content = form.cleaned_data.get("content")
            message.save()
            return redirect('/contact/list')
        else:
            return HttpResponse('해당하는 아이디가 존재하지 않습니다. 다시 확인해주세요.')
    else:
        form = MessageForm()
        return render(request, 'contact/contact_create.html', {'form': form})

def contact_recreate(request, message_id):
    sender_nickname = Message.objects.get(id=message_id).sender.nickname
    if request.method == 'POST':
        form = RemessageForm(request.POST)
        if form.is_valid():
            re_message = form.save(commit=False)
            re_message.sender = request.user
            re_message.recipient = Message.objects.get(id=message_id).sender
            re_message.message = Message.objects.get(id=message_id)
            re_message.content = form.cleaned_data.get("content")
            re_message.save()
            return redirect('/contact/list')
    else:
        form = RemessageForm()
        return render(request, 'contact/contact_recreate.html', {'form': form, 'sender_nickname': sender_nickname})

def contact_delete(request, message_id):
    message = Message.objects.get(pk=message_id)
    message.delete()
    return redirect('/contact/list')