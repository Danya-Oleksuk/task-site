from django.urls import path

from .views import user_tasks

app_name = "task_app"
urlpatterns = [
    path("user/tasks/", user_tasks, name="user_tasks"),
]
