from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from account.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import views as auth_views

def register(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("form save")
            # 신규 사용자를 저장한 후에 자동 로그인을 위해 개별적으로 email과 pw가져옴
            email = form.cleaned_data.get('email')
            print(email)
            raw_password = form.cleaned_data.get('password1')
            print(raw_password)
            user = authenticate(email=email, password=raw_password)
            print(user)
            login(request, user)
            return redirect('/')
    else:
        print("not valid form")
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

# class LoginView(auth_views.LoginView):
#     template_name = 'account/login.html'

#     def get_success_url(self):
#         return redirect('accounts:login')
# class LoginView(auth_views.LoginView):
#     form_class = LoginForm
#     template_name = 'account/login.html'
