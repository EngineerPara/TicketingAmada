from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    model=Post
    list_filter=['titolo','descr']
    list_display = ('titolo', 'descr',)
    search_fields= ['titolo', 'descr']


admin.site.register(Post, PostAdmin)