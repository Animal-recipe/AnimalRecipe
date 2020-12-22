from django import forms
from .models import AD, Service_center, Report_problem

class ADForm(forms.ModelForm):
    class Meta:
        model = AD
        fields = ['name', 'phone', 'content']

class Service_center_Form(forms.ModelForm):
    class Meta:
        model = Service_center
        fields = ['name', 'phone', 'content']

class Report_problem_Form(forms.ModelForm):
    class Meta:
        model = Report_problem
        fields = ['reason', 'other_reason']



