from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('send/', views.contact_create, name='contact_create'),
    path('list/', views.contact_list, name='contact_list'),
    path('detail/<int:contact_id>', views.contact_detail, name='contact_detail'),
    path('detail2/<int:contact_id>', views.contact_detail2, name='contact_detail2'),
    path('resend/<int:message_id>/', views.contact_recreate, name="contact_recreate"),
    path('delete/<int:message_id>/', views.contact_delete, name="contact_delete"),
]
