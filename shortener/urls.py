from django.urls import path
from . import views

urlpatterns = [
    path('', views.shorten_url, name='shorten_url'),
    path('result/<int:pk>/', views.result, name='result'),
    path('<str:short_code>/', views.redirect_url, name='redirect_url'),
]