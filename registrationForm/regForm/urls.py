from django.urls import path
from regForm import views

urlpatterns = [
    path('',views.registration,name="registration"),
    path('login',views.user_login,name='login'),
    path('home',views.home,name='home')
]
