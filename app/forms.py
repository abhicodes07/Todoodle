from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from .models import Todo, Task
from django.forms import formset_factory, inlineformset_factory


# register user
class CreateUserForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-all",
                "placeholder": "Enter your username",
            }
        )
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-all",
                "placeholder": "••••••••",
            }
        )
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-all",
                "placeholder": "••••••••",
            }
        )
    )

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]


# login a user
class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        widget=TextInput(
            attrs={
                "class": "w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-all",
                "placeholder": "Enter your username",
            }
        )
    )

    password = forms.CharField(
        widget=PasswordInput(
            attrs={
                "class": "w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-all",
                "placeholder": "••••••••",
            }
        )
    )


# todo form
class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = [
            "title",
            "description",
            "image",
            "author",
        ]


# update todo form
class TaskForm(forms.ModelForm):
    title = forms.CharField(
        widget=TextInput(
            attrs={
                "class": "w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-all",
                "placeholder": "Enter your username",
            }
        )
    )

    class Meta:
        model = Task
        fields = ["title", "completed"]


# Formset to handle multiple tasks linked to a Todo
TaskFromSet = inlineformset_factory(Todo, Task, form=TaskForm, extra=1)
