from django.urls import path
from .import views

app_name = 'mypage'

urlpatterns = [
    # path('/myRecipe', views.myRecipe, name="myRecipe"),
    # path('/myReview', views.myReview, name="myReview"),
    path('myQuestion/', views.myQuestion, name="myQuestion"),
    path('delete/myQuestion/<int:question_id>/', views.delete_myQuestion, name="delete_myQuestion"),
    # path('/myInfo', views.myRecipe, name="myInfo"),
]
