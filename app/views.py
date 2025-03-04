from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from django.shortcuts import get_object_or_404, redirect, render
from django.db import models

from app.models import Todo

from .forms import (
    CreateUserForm,
    LoginUserForm,
    TodoForm,
    TaskFromSet,
    UpdateTodoForm,
    UpdateTaskFormset,
)

# Create your views here.


# home page
def home(request):
    return render(request, "app/home.html")


# about section
def about(request):
    return render(request, "app/about.html")


# register
def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    return render(request, "app/register.html", context={"form": form})


def login_user(request):
    form = LoginUserForm()

    if request.method == "POST":
        form = LoginUserForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("")
    return render(request, "app/login.html", context={"form": form})


@login_required(login_url="login")
def dashboard(request):
    my_todos = Todo.objects.filter(user=request.user).annotate(
        task_count=models.Count("tasks")
    )
    return render(request, "app/dashboard.html", context={"todos": my_todos})


# create todo
@login_required(login_url="login")
def create_todo(request):
    todo_form = TodoForm()
    formset = TaskFromSet()

    if request.method == "POST":
        todo_form = TodoForm(request.POST, request.FILES)
        formset = TaskFromSet(request.POST)

        if todo_form.is_valid() and formset.is_valid():
            # save the todo first
            todo = todo_form.save(commit=False)  # prevent immediate DB save
            todo.user = request.user  # assign the todo to the logged in user
            todo.save()  # explicitly save todo

            tasks = formset.save(commit=False)  # get task instances but don't save yet

            for task in tasks:
                # prevent empty tasks from being saved
                if task.title.strip():
                    task.todo = todo  # link task to created todo
                    task.save()

            return redirect("dashboard")
    return render(
        request, "app/create_todo.html", {"todo_form": todo_form, "formset": formset}
    )


# update record
@login_required(login_url="login")
def update_todo(request, pk):
    todo = get_object_or_404(Todo, user=request.user, id=pk)
    update_todo_form = UpdateTodoForm(instance=todo)
    update_formset = UpdateTaskFormset(instance=todo)

    if request.method == "POST":
        update_todo_form = UpdateTodoForm(request.POST, request.FILES, instance=todo)
        update_formset = UpdateTaskFormset(request.POST, instance=todo)

        print("requested data: ", request.POST)

        if update_todo_form.is_valid() and update_formset.is_valid():
            update_todo_form.save()
            update_formset.save()
            return redirect("dashboard")
        else:
            print("Todo form error: ", update_todo_form.errors)
            print("udpate formset error: ", update_formset.errors)
    return render(
        request,
        "app/update.html",
        context={
            "update_todo_form": update_todo_form,
            "update_formset": update_formset,
        },
    )


# user logout
def logout_user(request):
    auth.logout(request)
    return redirect("login")
