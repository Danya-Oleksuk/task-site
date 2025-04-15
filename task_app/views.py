from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='/user/login')
async def user_tasks(request):
    tasks = ''
    return render(request, 'task_app/user_tasks.html', context={"tasks":tasks})