"""dataseven URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import re_path as url
from backend_api.views import *
from CompanyParser.views import PostCreateView, PostListView, PostRetrieveView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    
    path('api/company_search',  PostCreateView.as_view(), name='create_post'),
    path('api/getcompany',  PostListView.as_view(), name='find_all'),
    path('api/getcompany/<int:pk>/', PostRetrieveView.as_view(), name='find_one'),    path('api/token/', TokenObtainPairView.as_view()),
    
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('api/token/verify/', TokenVerifyView.as_view()),
    path('api/users/', include('users.urls')),
    path('admin/', admin.site.urls),
    path('', OneTestView.as_view(), name='oh shit')
]
