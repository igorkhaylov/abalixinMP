from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Ticker, Articles, Author, Categories, MainBlock, UzbNews, WorldNews, Video, Tests
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


class UzbNewsAdminForm(forms.ModelForm):
    description_ru = forms.CharField(label="Описание [ru]", widget=CKEditorUploadingWidget(config_name="my_config"))
    description_uz = forms.CharField(label="Описание [uz]", widget=CKEditorUploadingWidget(config_name="my_config"))

    class Meta:
        model = UzbNews
        fields = '__all__'


class WorldNewsAdminForm(forms.ModelForm):
    description_ru = forms.CharField(label="Описание [ru]", widget=CKEditorUploadingWidget(config_name="my_config"))
    description_uz = forms.CharField(label="Описание [uz]", widget=CKEditorUploadingWidget(config_name="my_config"))

    class Meta:
        model = WorldNews
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
    fieldsets = (
        ("Первый блок", {
            'fields': ('title', 'short_title', 'image', 'slug', 'categories', 'video')
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


@admin.register(UzbNews)
class UzbNewsAdmin(TranslationAdmin):
    list_display = ('short_title', 'title', )
    form = UzbNewsAdminForm
    save_on_top = True
    readonly_fields = ('date_created', 'views', )
    save_as = True


@admin.register(WorldNews)
class WorldNewsAdmin(TranslationAdmin):
    list_display = ('short_title', 'title', )
    form = UzbNewsAdminForm
    save_on_top = True
    readonly_fields = ('date_created', 'views', )
    save_as = True


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
        ("Лучшая статья", {
            'fields': ('bestArticle',)
        }),
        ("6 статей на выбор", {
            'fields': ('article7', 'article8', 'article9',
                       'article10', 'article11', 'article12',)
        }),
        )

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Video)
class VideoAdmin(TranslationAdmin):
    fieldsets = (
        ("Видео 1", {
            'fields': ('title1', 'link1', )
        }),
        ("Видео 2", {
            'fields': ('title2', 'link2',)
        }),
        ("Видео 3", {
            'fields': ('title3', 'link3',)
        }),
        ("Видео 4", {
            'fields': ('title4', 'link4',)
        }),
    )

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Tests)
class TestsAdmin(TranslationAdmin):
    list_display = ('title', )
    save_as = True


# admin.site.register(MainBlock)


admin.site.site_title = "Управление новостным сайтом"
admin.site.site_header = "Main Post"

