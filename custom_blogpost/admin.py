from django.contrib import admin

# Register your models here.

from copy import deepcopy
from django.contrib import admin
from mezzanine.blog.admin import BlogPostAdmin
from mezzanine.blog.models import BlogPost

blog_fieldsets = deepcopy(BlogPostAdmin.fieldsets)
blog_fieldsets[0][1]["fields"].insert(4, "user")

class MyBlogPostAdmin(BlogPostAdmin):
    fieldsets = blog_fieldsets

admin.site.unregister(BlogPost)
admin.site.register(BlogPost, MyBlogPostAdmin)