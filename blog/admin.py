from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("status", "created_on")
    list_display = ("title", "slug", "status", "created_on")
    search_fields = ("title", "content")
    summernote_fields = "content"
    actions = ["toggle_status"]

    def toggle_status(self, request, queryset):
        print(queryset)
        print(dir(queryset))
        for q in queryset:
            if q.status == 0:
                q.status = 1
                q.save()
            elif q.status == 1:
                q.status = 0
                q.save()


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    search_fields = ("name", "email", "body")
    list_filter = (
        "approved",
        "created_on",
    )
    list_display = ("name", "body", "post", "created_on", "approved")
    actions = ["approve_comments"]

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
