from django.shortcuts import render
from .models import AD, Service_center, Report_problem
from .forms import ADForm, Service_center_Form, Report_problem_Form
from django.shortcuts import redirect
from account.models import User
from django.contrib.auth.decorators import login_required

def create_AD(request):
    if request.method == 'POST':
        AD_form = ADForm(request.POST, request.FILES)
        if AD_form.is_valid():
            AD = AD_form.save(commit=False)
            AD.name = request.POST["name"]
            AD.phone = request.POST["phone"]
            AD.content = request.POST["content"]
            AD.save()
        return redirect('/')
    else:
        AD_form = ADForm()
    return render(request, '../templates/footer/AD.html')

def create_Service_center(request):
    if request.method == 'POST':
        Service_form = Service_center_Form(request.POST, request.FILES)
        if Service_form.is_valid():
            Service = Service_form.save(commit=False)
            Service.name = request.POST["name"]
            Service.phone = request.POST["phone"]
            Service.content = request.POST["content"]
            Service.save()
        return redirect('/')
    else:
        Service_form = Service_center_Form()
    return render(request, '../templates/footer/Service_center.html')

@login_required
def create_Report_problem(request, user_id):
    temp = User.objects.get(id=user_id).nickname
    if request.method == 'POST':
        Report_form = Report_problem_Form(request.POST)
        if Report_form.is_valid():
            Report = Report_form.save(commit=False)
            Report.author_id = request.user.id
            Report.target.id = user_id
            Report.reason = request.POST["reason"]
            Report.other_reason = request.POST["other_reason"]
            Report.save()
        return redirect('/')

    else:
        Report_form = Report_problem_Form()

    return render(request, '../templates/footer/Report_problem.html', {"user_id": temp})

def Terms_of_service(request):
    return render(request, '../templates/footer/Terms_of_service.html')

def Privacy_Policy(request):
    return render(request, '../templates/footer/Privacy_Policy.html')
