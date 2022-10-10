from django.contrib import admin

from assignment.models import Information, FileInformation


class InformationAdmin(admin.ModelAdmin):
    search_field = ['title', 'description']
    filterset_fields = ['title', 'description']
    list_display = ['title', 'description', 'image', 'created_at']


class FileInformationAdmin(admin.ModelAdmin):
    search_field = ['url']
    filterset_fields = ['url']
    list_display = ['url', 'created_at']


admin.site.register(Information, InformationAdmin)
admin.site.register(FileInformation, FileInformationAdmin)