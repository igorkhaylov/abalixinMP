from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Ticker, Articles, Author, Categories, MainBlock
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms


# config_name="my_config"
class ArticlesAdminForm(forms.ModelForm):
    description_ru = forms.CharField(label="Описание [ru]", widget=CKEditorUploadingWidget(config_name="my_config"))
    description_uz = forms.CharField(label="Описание [uz]", widget=CKEditorUploadingWidget(config_name="my_config"))

    class Meta:
        model = Articles
        fields = '__all__'


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
    form = ArticlesAdminForm
    save_on_top = True
    save_as = True
    # fields = (
    #     ('title', 'title1', 'title2', 'slug', ),
    #     ('image', 'categories', ),
    #     ('short_description', ),
    #     ('description', ),
    #     ('date_created',),
    #     ('author'), )
    fieldsets = (
        ("Первый блок", {
            'fields': ('title', 'short_title', 'image', 'slug', 'categories')
        }),
        ("Название из двух частей", {
            'fields': (('title1', 'title2',),)
        }),
        ("Описание", {
            'fields': ('short_description', 'description')
        }),
        ("Дата с автором", {
            'fields': ('date_created', 'author',)
        }),
    )
    readonly_fields = ('date_created', )
    prepopulated_fields = {'slug': ('title', )}


@admin.register(Author)
class AuthorAdmin(TranslationAdmin):
    list_display = ('name', )


@admin.register(Categories)
class CategoriesAdmin(TranslationAdmin):
    list_display = ('name', )
    prepopulated_fields = {'url': ('name', )}


@admin.register(MainBlock)
class MainBlockAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Главный блок статей", {
            'fields': ('firstArticle', 'secondArticle', 'thirdArticle',)
        }),
        ("6 статей на выбор", {
            'fields': ('article1', 'article2', 'article3',
                       'article4', 'article5', 'article6',)
        }),
    )

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


# admin.site.register(MainBlock)

