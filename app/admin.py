from django.contrib import admin
from .models import Todo, Task

# Register your models here.
# admin.site.register(Todo)


# edit tasks Inside the Todo Form
class TaskInline(admin.TabularInline):  # Use StackedInline for a different layout
    model = Task
    extra = 1  # Show one empty task form by default


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "creation_date", "updation_date")
    search_fields = ("title", "author")
    list_filter = ("creation_date", "updation_date")  # Adds filters in the sidebar
    ordering = ("-creation_date",)  # Show latest todos first
    readonly_fields = ("creation_date",)  # Prevent editing creation date


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "todo", "completed")
    search_fields = ("title", "todo__title")
    list_filter = ("completed",)
