from django.contrib import admin
from tasks.models import Project, Task
from quality_control.models import BugReport, FeatureRequest


class TaskInline(admin.TabularInline):
    model = Task
    extra = 0
    fields = ('name', 'description', 'assignee', 'status', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    can_delete = True
    show_change_link = True


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name', 'description')
    ordering = ('created_at',)
    date_hierarchy = 'created_at'

    inlines = [TaskInline]


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'project', 'assignee', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'assignee', 'project')
    search_fields = ('name', 'description')
    list_editable = ('status', 'assignee')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'project', 'task', 'status', 'priority', 'created_at', 'updated_at')
    list_filter = ('status', 'project', 'status', 'priority')
    search_fields = ('name', 'description')
    fieldsets = (
        (None, {
            'fields': ('title', 'project', 'task')
        }),
        ('Advanced options', {
            'fields': ('description', 'status', 'priority'),
        }),
    )
    list_editable = ('status',)


@admin.register(FeatureRequest)
class FeatureRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'project', 'task', 'status', 'priority', 'created_at', 'updated_at')
    list_filter = ('status', 'project', 'status', 'priority')
    search_fields = ('name', 'description')
    fieldsets = (
        (None, {
            'fields': ('title', 'project', 'task')
        }),
        ('Advanced options', {
            'fields': ('description', 'status', 'priority'),
        }),
    )


