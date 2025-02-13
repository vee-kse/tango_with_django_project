from django.contrib import admin
from rango.models import Category, Page

admin.site.register(Category)

class PageAdmin(admin.ModelAdmin):
    list_display = ('category', 'title', 'url')

admin.site.register(Page, PageAdmin)
