# vendor urls
from django.urls import path
from . import views
from accounts import views as accountsviews


urlpatterns = [
    path('', accountsviews.vendorDashboard, name='vdashboard'),
    path('profile/', views.vprofile, name='vprofile'),
]
