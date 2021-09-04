from django.db import models


class Articles(models.Model):
    short_title = models.CharField(max_length=120)
    title = models.CharField("Название статьи", max_length=250)
    title1 = models.CharField("Короткое название 1", max_length=120)
    title2 = models.CharField("Короткое название 2", max_length=120)
    image = models.ImageField("Картинка", upload_to="article/%Y/%m/%d/")
    slug = models.SlugField("Slug", max_length=120)
    categories = models.ForeignKey("Categories",
                                   verbose_name="Категории",
                                   on_delete=models.CASCADE,
                                   related_name="category")
    short_description = models.TextField("Короткое описание", max_length=250)
    description = models.TextField("Описание статьи")
    date_created = models.DateTimeField("Дата создания", auto_now_add=True)
    date_updated = models.DateTimeField("Дата обновления", auto_now=True)
    views = models.PositiveIntegerField("Просмотры", default=0)
    author = models.ForeignKey("Author", verbose_name="Автор", related_name="author", on_delete=models.CASCADE)
    # author = models.ManyToManyField("Author", verbose_name="Автор статьи", related_name="author")

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


class Author(models.Model):
    name = models.CharField("Имя", max_length=120)
    description = models.TextField("Описание", blank=True)

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


