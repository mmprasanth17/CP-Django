from django.contrib import admin
from .models import user,TagLine,Author,Comment

# Register your models here.
admin.site.register(TagLine)
admin.site.register(Author)
admin.site.register(user)
admin.site.register(Comment)
