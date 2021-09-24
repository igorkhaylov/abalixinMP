from modeltranslation.translator import register, TranslationOptions
from .models import Ticker, Articles, Author, Categories, UzbNews, WorldNews, Video, Tests, Podcasts


@register(Ticker)
class TickerTranslationOptions(TranslationOptions):
    fields = ('ticker', )


@register(Articles)
class ArticlesTranslationOptions(TranslationOptions):
    fields = (
        'short_title',
        'title',
        'title1',
        'title2',
        'short_description',
        'description',
    )


@register(UzbNews)
class UzbNewsTranslationOptions(TranslationOptions):
    fields = (
        'short_title',
        'title',
        'description',
    )


@register(WorldNews)
class WorldNewsTranslationOptions(TranslationOptions):
    fields = (
        'short_title',
        'title',
        'description',
    )


@register(Video)
class VideoTranslationOptions(TranslationOptions):
    fields = ('title1', 'title2', 'title3', 'title4', )


@register(Author)
class AuthorTranslationOptions(TranslationOptions):
    fields = ('name', 'description', )


@register(Categories)
class CategoriesTranslationOptions(TranslationOptions):
    fields = ('name', )


@register(Tests)
class TestsTranslationOptions(TranslationOptions):
    fields = ('title', 'description', )


@register(Podcasts)
class PodcastsTranslationOption(TranslationOptions):
    fields = ('title', 'genre', 'author', 'description', )

