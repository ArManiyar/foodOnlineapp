"""foodOnline_main URL Configuration

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
from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.myAccount, name='myAccount'),
    
    path('registerUser/', views.registerUser, name='registerUser'),
    path('registerVendor/', views.registerVendor, name='registerVendor'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    
    path('login/', views.handle_login, name='login'),
    path('logout/', views.handle_logout, name='logout'),
    
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('reset_password_validate/<uidb64>/<token>/', views.reset_password_validate, name='reset_password_validate'),
    path('reset_password/', views.reset_password, name='reset_password'),
    
    path('myAccount/', views.myAccount, name='myAccount'),
    path('vendordashboard/', views.vendorDashboard, name='vendorDashboard'),
    path('customerdashboard/', views.custDashboard, name='custDashboard'),
    
    path('vendor/', include('vendor.urls'), name='myrestaurant'),
    
  ]