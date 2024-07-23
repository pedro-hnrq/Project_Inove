from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_userId_name')
    search_fields = ('title',)

    def get_userId_name(self, obj):
        return obj.userId.name
    get_userId_name.short_description = 'User Name'
