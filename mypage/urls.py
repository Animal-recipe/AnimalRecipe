from django.urls import path
from .import views

app_name = 'mypage'

urlpatterns = [
    path('myRecipe/', views.myRecipe, name="myRecipe"),
    path('delete/myRecipe/<int:recipe_id>/', views.delete_myRecipe, name="delete_myRecipe"),
    path('saveRecipe/', views.saveRecipe, name="saveRecipe"),
    path('delete/saveRecipe/<int:recipe_id>/', views.delete_saveRecipe, name="delete_saveRecipe"),
    path('myQuestion/', views.myQuestion, name="myQuestion"),
    path('delete/myQuestion/<int:question_id>/', views.delete_myQuestion, name="delete_myQuestion"),
    path('myReview/', views.myReview, name="myReview"),
    path('delete/myReview/<int:review_id>/', views.delete_myReview, name="delete_myReview"),
    path('detail/myInfo', views.detail_myInfo, name="detail_myInfo"),
    path('update/myInfo', views.update_myInfo, name="update_myInfo"),
]
