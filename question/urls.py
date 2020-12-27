from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'question'

urlpatterns = [
    path('create/', views.question_create, name='create_question'),
    path('answer/create/<int:question_id>/', views.answer_create, name='create_answer'),
    path('list/', views.question_list, name='list'),
    path('detail/<int:question_id>/', views.question_detail, name='detail'),
    path("search/",views.search, name='search'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)