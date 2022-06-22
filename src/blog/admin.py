from django.contrib import admin

from .models import Article, Author, Tag, Note, Video
# Register your models here.

admin.site.register(Article)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Note)
admin.site.register(Video)
