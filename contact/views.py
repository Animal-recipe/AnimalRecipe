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

@login_required
def contact_create(request, user_id):
    sender_nickname = User.objects.get(id=user_id).nickname
    if request.method == 'POST':
        form = RemessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender_id = request.user.id
            message.recipient_id = user_id
            message.content = form.cleaned_data.get("content")
            message.save()
            return redirect('/contact/list')
        else:
            return HttpResponse('해당하는 아이디가 존재하지 않습니다. 다시 확인해주세요.')
    else:
        form = MessageForm()
        return render(request, 'contact/contact_recreate.html', {'form': form, 'sender_nickname': sender_nickname})

@login_required
def contact_recreate(request, message_id):
    sender_nickname = Message.objects.get(id=message_id).sender.nickname
    if request.method == 'POST':
        form = RemessageForm(request.POST)
        if form.is_valid():
            re_message = form.save(commit=False)
            re_message.sender = request.user
            re_message.recipient = Message.objects.get(id=message_id).sender
            re_message.content = form.cleaned_data.get("content")
            re_message.save()
            return redirect('/contact/list')
    else:
        form = RemessageForm()
        return render(request, 'contact/contact_recreate.html', {'form': form, 'sender_nickname': sender_nickname})

@login_required
def contact_delete(request, message_id):
    message = Message.objects.get(pk=message_id)
    if (message.recipient != request.user) and (message.sender != request.user): # 수신자 발신자가 모두 아닌 경우
        return redirect('/contact/list')
    else:
        message.delete()
    return redirect('/contact/list')

@login_required
def contact_senddelete(request):
    message = Message.objects.filter(recipient=request.user)
    for i in range(0, message.__len__()):
        if message[i].recipient != request.user:  # 발신자가 유저와 다른경우
            return redirect('/contact/list')
        else:
            message[i].delete()
    return redirect('/contact/list')

@login_required
def contact_receiveddelete(request):
    message = Message.objects.filter(sender=request.user)
    for i in range(0, message.__len__()):
        if message[i].sender != request.user:  # 수신자가 유저와 다른 경우
            return redirect('/contact/list')
        else:
            message[i].delete()
    return redirect('/contact/list')

@login_required
def contact_usersearch(request):
    q = request.POST.get('q', "")
    flag = 0
    if q:
        flag = 1
        username = User.objects.filter(nickname__icontains=q, is_active=True)

        return render(request, "contact/contact_usersearch.html", {'username': username, 'q': q, 'flag': flag})
    else:
        flag = 0
        return render(request, "contact/contact_usersearch.html", {'flag': flag})

@login_required
def contact_showsearch(request):
    return render(request, "contact/contact_usersearch.html")
