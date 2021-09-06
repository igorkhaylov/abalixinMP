from datetime import timezone, time
from django.utils import timezone

from django.db import models
# from ckeditor.fields import RichTextField
# from ckeditor_uploader.fields import RichTextUploadingField


class Articles(models.Model):
    short_title = models.CharField(max_length=120)
    title = models.CharField("Название статьи", max_length=250)
    title1 = models.CharField("Короткое название 1", max_length=120)
    title2 = models.CharField("Короткое название 2", max_length=120)
    image = models.ImageField("Картинка", upload_to="article/%Y/%m/%d/")
    slug = models.SlugField("Slug", max_length=120, unique=True)
    categories = models.ForeignKey("Categories",
                                   verbose_name="Категории",
                                   on_delete=models.CASCADE,
                                   related_name="category")
    short_description = models.TextField("Короткое описание", max_length=250)
    # description = RichTextUploadingField("Описание статьи", config_name="default")
    description = models.TextField("Описание статьи", )
    date_created = models.DateTimeField("Дата создания", default=timezone.now)   # auto_now_add=True
    date_updated = models.DateTimeField("Дата обновления", auto_now=True)        # auto_now=True
    views = models.PositiveIntegerField("Просмотры", default=0)
    author = models.ForeignKey("Author", verbose_name="Автор", related_name="author", on_delete=models.PROTECT)
    # author = models.ManyToManyField("Author", verbose_name="Автор статьи", related_name="author")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"


class News(models.Model):
    short_title = models.CharField(max_length=120)
    title = models.CharField("Название статьи", max_length=250)




class Ticker(models.Model):
    title = models.CharField("Бегущая строка", default="Бегущая строка", max_length=120, editable=False)
    ticker = models.CharField("Бегущая строка", max_length=500)

    class Meta:
        verbose_name = "Бегущая строка"
        verbose_name_plural = "Бегущая строка"


class Author(models.Model):
    name = models.CharField("Имя", max_length=120)
    description = models.TextField("Описание", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


class Categories(models.Model):
    name = models.CharField("Название категории", max_length=120)
    url = models.SlugField(max_length=120, unique=True)
    # tag = models.ForeignKey("")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class MainBlock(models.Model):
    firstArticle = models.ForeignKey("Articles", verbose_name="Первая статья", related_name="firstArticle", on_delete=models.PROTECT)
    secondArticle = models.ForeignKey("Articles", verbose_name="Вторая статья", related_name="secondArticle", on_delete=models.PROTECT)
    thirdArticle = models.ForeignKey("Articles", verbose_name="Третья статья", related_name="thirdArticle", on_delete=models.PROTECT)

    def __str__(self):
        return "Главная страница"

    class Meta:
        verbose_name = "Главная страница"
        verbose_name_plural = "Главная страница"
