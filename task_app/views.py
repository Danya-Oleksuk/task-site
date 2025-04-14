from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


@login_required(login_url='/user/login')
def user_tasks(request):
    data = ''
    return render(request, 'task_app/user_tasks.html', context={"data":data})