from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import Recipe_Like, Recipe_Save, Recipe_Like2, Recipe_Save2

app_name = 'recipe'

urlpatterns = [
    path('list/', views.recipe_list, name='list_recipe'),
    path('create/', views.create, name='create_recipe'),
    path('detail/<int:recipe_id>/', views.recipe_detail, name='detail_recipe'),
    path('delete/<int:recipe_id>/', views.delete, name='delete_recipe'),
    path('edit/<int:recipe_id>/', views.edit, name='edit_recipe'),
    path('like/<int:recipe_id>/', Recipe_Like.as_view(), name='like_recipe'),
    path('like2/<int:recipe_id>/', Recipe_Like2.as_view(), name='like_recipe2'),
    path('save_count/<int:recipe_id>/', Recipe_Save.as_view(), name='save_recipe'),
    path('save_count2/<int:recipe_id>/', Recipe_Save2.as_view(), name='save_recipe2'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
