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
    list_display = ("title", "user", "creation_date", "updation_date")
    search_fields = ("title", "user__username")  # search by user's username
    list_filter = ("creation_date", "updation_date")  # Adds filters in the sidebar
    ordering = ("-creation_date",)  # Show latest todos first
    readonly_fields = ("creation_date",)  # Prevent editing creation date

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:  # Allow superusers to see all Todos
            return qs
        return qs.filter(user=request.user)  # Normal users see only their Todos


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "todo", "completed")
    search_fields = ("title", "todo__title")
    list_filter = ("completed",)
