from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("", include('service.urls')),  # адреса приложения
    path("", include('api.urls')),  # адреса API
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")),
]
