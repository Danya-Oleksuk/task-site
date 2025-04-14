from asgiref.sync import sync_to_async
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .forms import LoginForm

from .database import is_user_in_database, get_user_profile

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
                    await sync_to_async(request.session.__setitem__)('user_id', username)
                    return redirect('/user/tasks')
                else:
                    error_message = 'Пароль не верен'
            else:
                error_message = 'Логин не существует'
    else:
        form = LoginForm()
    return render(request, 'user_app/user_login.html', {'form': form,
                                                                            'error_message': error_message})

def user_tasks(request):
    if not request.session.get('user_id'):
        return redirect('/user/login')

    data = ''
    return render(request, 'user_app/user_tasks.html', context={"data":data})