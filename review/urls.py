from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import Review_Like

app_name = 'review'

urlpatterns = [
    path('list/', views.review_list, name='list_review'),
    path('create/<int:recipe_id>/', views.create, name='create_review'),
    path('detail/<int:review_id>/', views.review_detail, name='detail_review'),
    path('delete/<int:review_id>/', views.delete, name='delete_review'),
    path('edit/<int:review_id>/', views.edit, name='edit_review'),
    path('like/<int:review_id>/', Review_Like.as_view(), name='like_review'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
