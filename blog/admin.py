from django.contrib import admin
from .models import Author, Post, Tag, Comment

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_filter = ("last_name",)
    list_display = ("full_name", "e_mail")
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "title", "tags")
    list_display = ("title", "date", "author")

class CommentAdmin(admin.ModelAdmin):
    list_display = ("user_name", "posts")

admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)
