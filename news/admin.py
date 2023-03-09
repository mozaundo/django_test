from django.contrib import admin
from .models import News

admin.site.register(News)

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title')

# Register your models here.
