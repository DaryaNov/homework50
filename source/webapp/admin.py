from django.contrib import admin
from webapp.models import Article, Type, Status, Project


admin.site.register(Article)
admin.site.register(Type)
admin.site.register(Status)
admin.site.register(Project)