from django.urls import path
from . import views

app_name = 'footer'

urlpatterns = [
    path('AD/', views.create_AD, name='AD'),
    path('Report/<user_id>/', views.create_Report_problem, name='Report'),
    path('Service/', views.create_Service_center, name='Service'),
    path('Terms_of_service/', views.Terms_of_service, name='Terms'),
    path('Privacy_Policy/', views.Privacy_Policy, name='Privacy'),
]

