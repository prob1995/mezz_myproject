from django.contrib import admin

# Register your models here.
from django.db import models
from copy import deepcopy
from django.contrib import admin
from mezzanine.blog.admin import BlogPostAdmin
from mezzanine.core.models import Displayable
from mezzanine.blog.models import BlogPost
from mezzanine.blog.admin import BlogPostAdmin

blog_fieldsets = deepcopy(BlogPostAdmin.fieldsets)
blog_fieldsets[0][1]["fields"].insert(4, "user")


class MyBlogPostAdmin(BlogPostAdmin):
    fieldsets = blog_fieldsets

    def get_changeform_initial_data(self, request):
        return {'status': 1, 'allow_comments': False}


admin.site.unregister(BlogPost)
admin.site.register(BlogPost, MyBlogPostAdmin)