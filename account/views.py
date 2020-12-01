from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from account.forms import UserCreationForm, UserChangeForm


def register(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # 신규 사용자를 저장한 후에 자동 로그인을 위해 개별적으로 email과 pw가져옴
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'account/register.html', {'form': form})

def mypage(request):

    if request.method == "POST":
        form = UserChangeForm(request.POST)
        if form.is_valid():
            form.save()
            # 신규 사용자를 저장한 후에 자동 로그인을 위해 개별적으로 email과 pw가져옴
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserChangeForm()
    return render(request, 'account/mypage.html', {'form': form})


