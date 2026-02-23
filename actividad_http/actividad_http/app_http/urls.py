from django.urls import path
from .views import equipos_view

urlpatterns = [
    path('equipos/', equipos_view),
]