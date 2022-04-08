from django.contrib import admin

from .models import Article,Category
# Register your models here.

class CategoryInLine(admin.StackedInline):
    model = Category
    extra = 1

class ArticleAdmin(admin.ModelAdmin):
    fields = ['author', 'title', 'content']
    inlines = [CategoryInLine]

admin.site.register(Article, ArticleAdmin)