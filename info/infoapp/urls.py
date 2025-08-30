from django.urls import path
from infoapp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("",views.index,name='index'),
    path('display',views.display,name='display'),
    path('profile',views.profile,name='profile'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
