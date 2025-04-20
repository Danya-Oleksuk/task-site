from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.shortcuts import render

from .mongo import count_tasks, create_mongo_database, get_tasks


@login_required(login_url="/user/login", redirect_field_name=None)
def user_tasks(request):
    create_mongo_database()

    tasks = cache.get("user_tasks")
    count = cache.get("count_tasks")
    if not tasks:
        tasks = get_tasks(user_id=int(request.user.username))
        cache.set("user_tasks", tasks, timeout=5)

        count = count_tasks(user_id=int(request.user.username))
        cache.set("count_tasks", count, timeout=5)

    return render(
        request,
        "task_app/user_tasks.html",
        context={
            "tasks": tasks,
            "count_tasks": count,
        },
    )
