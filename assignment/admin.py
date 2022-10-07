from django.contrib import admin

from assignment.models import Information


class InformationAdmin(admin.ModelAdmin):
    search_field = ['title', 'description']
    filterset_fields = ['title', 'description']
    list_display = ['title', 'description', 'image', 'created_at']

admin.site.register(Information, InformationAdmin)