from django.urls import path
from carsapp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.showProduct,name="companies"),
    path('<int:id>',views.company_details,name='details')
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
