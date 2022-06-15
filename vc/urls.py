from django.urls import path

from . import views

app_name = "vc"

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('add/', views.add, name='add'),
    path('<str:person_name>/', views.page, name='page'),
]