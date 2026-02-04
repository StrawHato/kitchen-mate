from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("kitchen/", include("kitchen.urls", namespace="kitchen")),
    path("accounts/", include("django.contrib.auth.urls")),
] + debug_toolbar_urls()
