from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.models import BaseInlineFormSet

# ClearableFileInput for taking file inputs
from django.forms.widgets import (
    PasswordInput,
    TextInput,
    ClearableFileInput,
    CheckboxInput,
)
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
                "class": "w-full p-3 border text-white border-white rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-blue-500 transition-all bg-transparent placeholder-gray-500",
                "placeholder": "Enter title of todo",
            }
        )
    )

    description = forms.CharField(
        widget=TextInput(
            attrs={
                "class": "w-full p-3 border border-white text-white rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-blue-500 transition-all bg-transparent placeholder-gray-500",
                "placeholder": "Enter description",
            }
        ),
        max_length=400,
    )

    image = forms.ImageField(
        required=False,
        widget=ClearableFileInput(
            attrs={
                "class": "block w-full p-3 text-sm text-white border border-white rounded-lg cursor-pointer bg-transparent focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-all placeholder-gray-500",
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
                "class": "flex w-full p-3 border-4 border-white text-white rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-blue-500 transition-all bg-transparent placeholder-gray-700",
                "placeholder": "Enter title of task",
            }
        )
    )

    class Meta:
        model = Task
        fields = ["title", "completed"]


# update task form
class UpdateTodoForm(forms.ModelForm):
    title = forms.CharField(
        widget=TextInput(
            attrs={
                "class": "w-full p-3 border text-white border-white rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-blue-500 transition-all bg-transparent placeholder-gray-500",
                "placeholder": "Enter title of todo",
            }
        )
    )

    description = forms.CharField(
        widget=TextInput(
            attrs={
                "class": "w-full p-3 border border-white text-white rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-blue-500 transition-all bg-transparent placeholder-gray-500",
                "placeholder": "Enter description",
            }
        ),
        max_length=400,
    )

    image = forms.ImageField(
        required=False,
        widget=ClearableFileInput(
            attrs={
                "class": "block w-full p-3 text-sm text-white border border-white rounded-lg cursor-pointer bg-transparent focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-all placeholder-gray-500",
                "accept": "image/*",  # accept only image file
            }
        ),
    )

    class Meta:
        model = Todo
        fields = ["title", "description", "image"]


# update task form
class UpdateTaskForm(forms.ModelForm):
    title = forms.CharField(
        widget=TextInput(
            attrs={
                "class": "flex w-full p-3 border-4 border-white text-white rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-blue-500 transition-all bg-transparent placeholder-gray-700",
                "placeholder": "Enter title of task",
            }
        )
    )

    class Meta:
        model = Task
        fields = ["title", "completed"]
        widgets = {
            "id": forms.HiddenInput(),  # render id as hidden field
            "completed": CheckboxInput(
                attrs={
                    "class": "w-5 h-5 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500",
                }
            ),
        }


class BaseTaskInlineFormSet(BaseInlineFormSet):
    def _construct_form(self, i, **kwargs):
        form = super()._construct_form(i, **kwargs)
        # For extra forms (i.e. forms after the initial ones), allow them to be empty.
        if i >= self.initial_form_count():
            form.empty_permitted = True
        return form


# Formset to handle and update multiple tasks
UpdateTaskFormset = inlineformset_factory(
    Todo, Task, form=UpdateTaskForm, extra=0, can_delete=True, formset=BaseInlineFormSet
)

# Formset to handle multiple tasks linked to a Todo
TaskFromSet = inlineformset_factory(Todo, Task, form=TaskForm, extra=1, can_delete=True)
