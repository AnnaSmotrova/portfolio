from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'technology', 'is_published', 'star_count', 'created_on')
    list_filter = ('technology', 'is_published', 'created_on')
    search_fields = ('title', 'description')
    list_editable = ('is_published',)
    readonly_fields = ('star_count', 'fork_count')