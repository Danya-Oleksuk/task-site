from django.http import HttpResponse
from django.urls import path

urlpatterns = [
    path('tasks/', lambda request: HttpResponse('Good tasks'))
]
