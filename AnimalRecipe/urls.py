"""AnimalRecipe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls'), name='home'),
    path('contact/', include('contact.urls'), name='contact'),
    path('recipe/', include('recipe.urls'), name='recipe'),
    path('review/', include('review.urls'), name='review'),
    path('question/', include('question.urls'), name='question'),
    path('account/', include('account.urls'), name='account'),
    path('about/', include('about.urls'), name="about"),
    path('footer/', include('footer.urls'), name="footer"),
    path('mypage/', include('mypage.urls'), name="mypage"),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'home.views.page_not_found'
handler500 = 'home.views.server_error_page'
