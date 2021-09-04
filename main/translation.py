from modeltranslation.translator import register, TranslationOptions
from .models import Ticker, Articles, Author, Categories


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


@register(Author)
class AuthorTranslationOptions(TranslationOptions):
    fields = ('name', 'description', )


@register(Categories)
class CategoriesTranslationOptions(TranslationOptions):
    fields = ('name', )



