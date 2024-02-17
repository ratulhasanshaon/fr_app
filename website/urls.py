
from django.contrib import admin
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include  

urlpatterns = [
    path('', views.login_redirect), 
    path('admin/', admin.site.urls),  
    path('home/', include('home.urls')), 
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)