from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)



# Register your models here.
#admin.site.register(Post)
# Note: This will allow you to create, update and delete blog posts from the admin panel. 
# However, please refrain from adding any posts at the moment, 
# as there are more fields to be added to the tables in an upcoming topic.
admin.site.register(Comment)