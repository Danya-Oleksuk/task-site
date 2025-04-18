from asgiref.sync import sync_to_async
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from .database import get_user_profile, is_user_in_database
from .forms import LoginForm


class MainPageView(TemplateView):
    template_name = 'main_page.html'

    def get_context_data(self, **kwargs):
        context = super(MainPageView, self).get_context_data(**kwargs)
        context['title'] = 'Task manager'
        return context

async def user_login(request):
    error_message = None

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = int(form.cleaned_data['username'])
            password = form.cleaned_data['password']

            if await is_user_in_database(username):
                data = await get_user_profile(username)

                if data[0] == username and data[1] == password:
                    user = await User.objects.filter(username=username).afirst()

                    if not user:
                        user = User(username=username)
                        user.set_password(password)
                        await sync_to_async(user.save)()

                    await sync_to_async(login)(request, user)
                    return redirect('/user/tasks')
            else:
                error_message = 'Логин не существует'
    else:
        form = LoginForm()
    return render(request, 'user_app/user_login.html', {'form': form,
                                                                            'error_message': error_message})

class LogOutView(LogoutView):
    next_page = reverse_lazy('user_app:main_page')