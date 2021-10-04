import datetime

from django.utils import timezone
from django.db import models
# from ckeditor.fields import RichTextField
# from ckeditor_uploader.fields import RichTextUploadingField


class Articles(models.Model):
    short_title = models.CharField("Короткое название", max_length=120)
    video = models.CharField("Ссылка YouTube", max_length=500, blank=True)
    title = models.CharField("Название статьи", max_length=250)
    title1 = models.CharField("Короткое название 1", max_length=120)
    title2 = models.CharField("Короткое название 2", max_length=120)
    image = models.ImageField("Картинка", upload_to="article/%Y/%m/%d/")
    slug = models.SlugField("Slug", max_length=120, unique=True)
    categories = models.ForeignKey("Categories",
                                   verbose_name="Категории",
                                   on_delete=models.CASCADE,
                                   related_name="category")
    short_description = models.TextField("Короткое описание", max_length=300)
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
        # ordering = ["-date_created"]
        ordering = ["-id"]


class UzbNews(models.Model):
    short_title = models.CharField(max_length=120)
    title = models.CharField("Название статьи", max_length=250)
    image = models.ImageField("Картинка", upload_to="uzbnews/%Y/%m/%d/", blank=True)
    description = models.TextField("Описание")
    views = models.IntegerField("Просмотры", default=0)
    date_created = models.DateTimeField("Дата создания", default=timezone.now)   # auto_now_add=True
    date_updated = models.DateTimeField("Дата обновления", auto_now=True)        # auto_now=True

    def __str__(self):
        return self.short_title

    class Meta:
        verbose_name = "Новости Узбекистана"
        verbose_name_plural = "Новости Узбекистана"


class WorldNews(models.Model):
    short_title = models.CharField(max_length=120)
    title = models.CharField("Название новости", max_length=250)
    image = models.ImageField("Картинка", upload_to="worldnews/%Y/%m/%d/", blank=True)
    description = models.TextField("Описание")
    views = models.IntegerField("Просмотры", default=0)
    date_created = models.DateTimeField("Дата создания", default=timezone.now)   # auto_now_add=True
    date_updated = models.DateTimeField("Дата обновления", auto_now=True)        # auto_now=True

    def __str__(self):
        return self.short_title

    class Meta:
        verbose_name = "Мировые Новости"
        verbose_name_plural = "Мировые новости"
        ordering = ["-date_created"]


class Ticker(models.Model):
    title = models.CharField("Бегущая строка", default="Бегущая строка", max_length=120, editable=False)
    ticker = models.CharField("Бегущая строка", max_length=500)

    def __str__(self):
        return self.title

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
    description = models.TextField("Описание", max_length=250)
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

    article1 = models.ForeignKey("Articles", verbose_name="Статья 1", related_name="article1", on_delete=models.PROTECT)
    article2 = models.ForeignKey("Articles", verbose_name="Статья 2", related_name="article2", on_delete=models.PROTECT)
    article3 = models.ForeignKey("Articles", verbose_name="Статья 3", related_name="article3", on_delete=models.PROTECT)
    article4 = models.ForeignKey("Articles", verbose_name="Статья 4", related_name="article4", on_delete=models.PROTECT)
    article5 = models.ForeignKey("Articles", verbose_name="Статья 5", related_name="article5", on_delete=models.PROTECT)
    article6 = models.ForeignKey("Articles", verbose_name="Статья 6", related_name="article6", on_delete=models.PROTECT)

    podcast = models.ForeignKey("Podcasts", verbose_name="Подкаст", related_name="podcast", on_delete=models.PROTECT)

    article7 = models.ForeignKey("Articles", verbose_name="Статья 1", related_name="article7", on_delete=models.PROTECT)
    article8 = models.ForeignKey("Articles", verbose_name="Статья 2", related_name="article8", on_delete=models.PROTECT)
    article9 = models.ForeignKey("Articles", verbose_name="Статья 3", related_name="article9", on_delete=models.PROTECT)
    article10 = models.ForeignKey("Articles", verbose_name="Статья 4", related_name="article10", on_delete=models.PROTECT)
    article11 = models.ForeignKey("Articles", verbose_name="Статья 5", related_name="article11", on_delete=models.PROTECT)
    article12 = models.ForeignKey("Articles", verbose_name="Статья 6", related_name="article12", on_delete=models.PROTECT)

    bestArticle = models.ForeignKey("Articles", verbose_name="Лучшая статья", related_name="bestArticle", on_delete=models.PROTECT)


    def __str__(self):
        return "Главная страница"

    class Meta:
        verbose_name = "Главная страница"
        verbose_name_plural = "Главная страница"


class Video(models.Model):
    title1 = models.CharField("Название видео 1", max_length=250)
    link1 = models.CharField("Ссылка на видео 1", max_length=250)
    title2 = models.CharField("Название видео 2", max_length=250)
    link2 = models.CharField("Ссылка на видео 2", max_length=250)
    title3 = models.CharField("Название видео 3", max_length=250)
    link3 = models.CharField("Ссылка на видео 3", max_length=250)
    title4 = models.CharField("Название видео 4", max_length=250)
    link4 = models.CharField("Ссылка на видео 4", max_length=250)

    def __str__(self):
        return "ВИДЕО"

    class Meta:
        verbose_name = "ВИДЕО"
        verbose_name_plural = "ВИДЕО"


class Tests(models.Model):
    title = models.CharField("Название", max_length=120)
    description = models.TextField("Описание")
    picture = models.ImageField("Картинка", upload_to="tests/%Y/%m/%d/")
    questions = models.IntegerField("Количество вопросов", default=0)
    passage_time = models.SmallIntegerField("Время прохождения мин", default=0)
    link = models.CharField("Ссылка на тест", max_length=250)
    date = models.DateTimeField("Дата и время")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Тесты"
        verbose_name_plural = "Тесты"


class Podcasts(models.Model):
    title = models.CharField("Название", max_length=50)
    genre = models.CharField("Жанр", max_length=50)
    author = models.CharField("Автор", max_length=100)
    description = models.TextField("Описание", blank=True)
    file = models.FileField("Аудио файл", upload_to="podcasts_audio/", blank=True)
    image = models.ImageField("Картинка", upload_to="podcasts/%Y/%m/%d/")
    link = models.CharField("Сылка", max_length=250)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Подкаст"
        verbose_name_plural = "Подкасты"
