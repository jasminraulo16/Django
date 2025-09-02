from django.urls import path
from regForm import views

urlpatterns = [
    path('',views.registration,name="registration"),
    path('login',views.user_login,name='login'),
    path('logout',views.user_logout,name='logout'),
    path('profile',views.profile, name='profile'),
    path('home',views.home,name='home')
]
