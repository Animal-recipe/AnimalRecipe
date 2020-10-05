from django.urls import path
from . import views

urlpatterns = [
    path('', views.listMessage, name='listMessage'),
    path('detail/<int:message_id>', views.viewMessage, name='viewMessage'),
    path('send/', views.sendMessage, name='sendMessage'),
    path('test/', views.test, name='test'),
    path('create_recomment/<int:message_id>', views.create_remessage, name="create_remessage"),

]

