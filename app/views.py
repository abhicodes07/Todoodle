from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from django.forms import Form
from django.shortcuts import redirect, render

from app.models import Todo

from .forms import CreateUserForm, LoginUserForm, TodoForm, TaskFromSet

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
    my_todos = Todo.objects.all()
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
            todo = todo_form.save()  # save the todo first
            tasks = formset.save(commit=False)  # get task instances but don't save yet

            for task in tasks:
                task.todo = todo  # link task to created todo
                task.save()

        # return redirect('dashboard')
    return render(
        request, "app/create_todo.html", {"todo_form": todo_form, "formset": formset}
    )


# user logout
def logout_user(request):
    auth.logout(request)
    return redirect("login")
