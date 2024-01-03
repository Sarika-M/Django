from django.contrib import admin
from .models import Task

# Register your models here.
class admin_panel(admin.ModelAdmin):
    list_display=('task','is_completed','updated_at')
    search_fields=('task',)
admin.site.register(Task,admin_panel)
