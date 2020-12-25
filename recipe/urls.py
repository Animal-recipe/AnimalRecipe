from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'recipe'

urlpatterns = [
    path('list/', views.recipe_list, name='list_recipe'),
    path('create/', views.create, name='create_recipe'),
    path('detail/<int:recipe_id>/', views.recipe_detail, name='detail_recipe'),
    path('delete/<int:recipe_id>/', views.delete, name='delete_recipe'),
    path('edit/<int:recipe_id>/', views.edit, name='edit_recipe'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

