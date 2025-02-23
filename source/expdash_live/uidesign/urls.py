from django.urls import path 
from django.contrib import admin
from uidesign import views
import os


urlpatterns = [
    path("admin/", admin.site.urls),  # Admin panel
    path("", views.loadTemplate, name="Template_Homepage"),  # Your existing route
]