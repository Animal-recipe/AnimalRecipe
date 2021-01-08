from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('send/<int:user_id>', views.contact_create, name='contact_create'),
    path('list/', views.contact_list, name='contact_list'),
    path('detail/<int:contact_id>', views.contact_detail, name='contact_detail'),
    path('detail2/<int:contact_id>', views.contact_detail2, name='contact_detail2'),
    path('resend/<int:message_id>/', views.contact_recreate, name="contact_recreate"),
    path('delete/<int:message_id>/', views.contact_delete, name="contact_delete"),
    path('senddelete/', views.contact_senddelete, name="contact_senddelete"),
    path('receiveddelete/', views.contact_receiveddelete, name="contact_receiveddelete"),
    path('usersearch/', views.contact_usersearch, name="contact_usersearch"),
    path('showsearch/', views.contact_showsearch, name="contact_showsearch"),
]
