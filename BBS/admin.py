from django.contrib import admin
from .models import *

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','title','author','hidden','publish_date')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','parent_comment','comment','date')


admin.site.register(Article,ArticleAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(UserProfile)
admin.site.register(UserGroup)