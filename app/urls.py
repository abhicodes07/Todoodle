from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name=""),
    path("about/", views.about, name="about"),
    path("register/", views.register, name="register"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("todo/", views.create_todo, name="todo"),
    path("update/<int:pk>/", views.update_todo, name="update"),
    path("delete/<int:pk>/", views.delete_todo, name="delete"),
]
