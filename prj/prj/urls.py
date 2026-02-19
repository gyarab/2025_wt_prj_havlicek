from django.contrib import admin
from django.urls import path, include  # přidáme include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),   # všechno ostatní pošle do app
]
