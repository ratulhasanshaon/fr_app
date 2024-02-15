
from django.contrib import admin
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include  # Importing path instead of url

urlpatterns = [
    path('', views.login_redirect),  # Using path instead of url
    path('admin/', admin.site.urls),  # Using path instead of url
    path('home/', include('home.urls')),  # Using path instead of url
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
