from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Ticker, Articles, Author, Categories


@admin.register(Ticker)
class TickerAdmin(TranslationAdmin):
    list_display = ('title', 'ticker',)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Articles)
class ArticlesAdmin(TranslationAdmin):
    list_display = ('title', 'short_title',)


@admin.register(Author)
class AuthorAdmin(TranslationAdmin):
    list_display = ('name', )


@admin.register(Categories)
class CategoriesAdmin(TranslationAdmin):
    list_display = ('name', )
    prepopulated_fields = {'url': ('name', )}



