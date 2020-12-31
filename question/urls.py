from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'question'

urlpatterns = [
    path('create/', views.question_create, name='create_question'),
    path('update/<int:question_id>/', views.update_question, name='update_question'),
    path('delete/<int:question_id>/', views.delete_question, name='delete_question'),
    path('create/answer/<int:question_id>/', views.create_answer, name='create_answer'),
    path('update/asnwer/<int:answer_id>/', views.update_answer, name='update_answer'),
    path('delete/answer/<int:answer_id>/', views.delete_answer, name='delete_answer'),
    path('accept/answer/<int:answer_id>/', views.accept, name="accept"),
    path('list/', views.question_list, name='list'),
    path('detail/<int:question_id>/', views.question_detail, name='detail'),
    path("search/",views.search, name='search'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
