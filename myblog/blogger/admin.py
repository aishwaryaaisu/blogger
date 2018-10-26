from django.contrib import admin

from blogger.models import blogpost,Comment
admin.site.register(blogpost)
admin.site.register(Comment)