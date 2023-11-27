from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('', views.hello, name='hello'),
    path('logout/', views.logout_view, name='logout'),
    path('registration/', views.user_registration, name='registration'),
]
