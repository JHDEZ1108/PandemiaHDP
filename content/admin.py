from django.contrib import admin
from .models import Comment

class CommentAdmin(admin.ModelAdmin):
  readonly_fields = ("created", )

# Register your models here.
admin.site.register(Comment, CommentAdmin)