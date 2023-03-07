from django.contrib import admin
from .models import MenuItem
from django.template.defaultfilters import slugify


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": (slugify("name"),)}
    list_display = ('name', 'parent', 'depth')
    exclude = ('depth',)
