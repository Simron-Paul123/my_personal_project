from django.contrib import admin
from django.urls import include, path
from event import views


urlpatterns = [
    path('', views.home, name='home'),path('website1/', views.website1, name='website1'),path('dept1/', views.dept1, name='dept1'),path('IT/', views.IT, name='IT'),path('signup/', views.SignupPage, name='signup'),path('login/', views.LoginPage, name='login'),
]