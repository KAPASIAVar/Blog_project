"""
URL configuration for My_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from application import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Sign_up/',views.Sign_up,name='Sign_up'),
    path('home/', views.home, name='home'),
    path('input/', views.input, name='input'),
    path('Blog/<str:blog_id>/<str:blog_category_name>/', views.View, name='Blog'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', views.Login, name='Login'),
    path('logout', views.Logout, name='logout'),
    path('change_password', views.Change_Password, name='change_password'),
    path('View_blog/<int:blog_id>/', views.View_blog, name='View_blog'),
    #path("accounts/", include("django.contrib.auth.urls")), #yeah account login and logout karne ke kam aata h
]
if settings.DEBUG:
        urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
