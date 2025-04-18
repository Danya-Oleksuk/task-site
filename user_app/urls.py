from django.urls import path

from .views import LogOutView, MainPageView, user_login

app_name = 'user_app'
urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),
    path('user/login/', user_login, name='user_login'),
    path('user/logout/', LogOutView.as_view(), name='user_logout'),
]
