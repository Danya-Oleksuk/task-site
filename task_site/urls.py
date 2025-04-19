from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("user_app.urls")),
    path("", include("task_app.urls")),
]
