from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'review'

urlpatterns = [
    path('list/', views.review_list, name='list_review'),
    path('create/<int:recipe_id>/', views.create, name='create_review'),
    path('detail/<int:review_id>/', views.review_detail, name='detail_review'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)