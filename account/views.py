from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from account.forms import UserCreationForm, UserChangeForm, LoginForm
from django.contrib.auth import views as auth_views
from django.contrib import messages

def register(request):
    if request.method == "GET":
        if 'agreement' not in request.session:
            return redirect('/account/agreement/')
        else:
            form = UserCreationForm()
    elif request.method == "POST":
        form = UserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('/account/register/success/')
        else:
            pass
    return render(request, 'account/register.html', {'form': form})

def agreement(request, *args, **kwargs):
    if request.method == "GET":
        return render(request, 'account/agreement.html')
    elif request.method == "POST":
        if request.POST.get('agreement1', False) and request.POST.get('agreement2', False):
            request.session['agreement'] = True
            return redirect('/account/register/')
        else:
            return render(request, 'account/agreement.html')
def registerSuccess(request):
    if request.method == "GET":
        return render(request, 'account/registerSuccess.html')
def mypage(request):
    if request.method == "POST":
        form = UserChangeForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect('/')
    else:
        form = UserChangeForm()
    return render(request, 'account/mypage.html', {'form': form})

def mylogin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(request, email=email, password=password)
            login(request, user)
            return redirect('/')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})
