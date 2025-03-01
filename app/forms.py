from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms

# ClearableFileInput for taking file inputs
from django.forms.widgets import PasswordInput, TextInput, ClearableFileInput
from .models import Todo, Task
from django.forms import inlineformset_factory


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
    title = forms.CharField(
        widget=TextInput(
            attrs={
                "class": "w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-all",
                "placeholder": "Enter title of todo",
            }
        )
    )

    description = forms.CharField(
        widget=TextInput(
            attrs={
                "class": "w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-all",
                "placeholder": "Enter description",
            }
        ),
        max_length=400,
    )

    image = forms.ImageField(
        required=False,
        widget=ClearableFileInput(
            attrs={
                "class": "block w-full p-3 text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500",
                "accept": "image/*",  # accept only image file
            }
        ),
    )

    class Meta:
        model = Todo
        fields = [
            "title",
            "description",
            "image",
        ]


# update todo form
class TaskForm(forms.ModelForm):
    title = forms.CharField(
        widget=TextInput(
            attrs={
                "class": "w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-all",
                "placeholder": "Enter title of task",
            }
        )
    )

    class Meta:
        model = Task
        fields = ["title", "completed"]


# Formset to handle multiple tasks linked to a Todo
TaskFromSet = inlineformset_factory(Todo, Task, form=TaskForm, extra=1)
