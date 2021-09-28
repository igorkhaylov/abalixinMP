from django.shortcuts import render, get_object_or_404
from .models import Ticker, MainBlock, Articles, UzbNews, Video, Tests, WorldNews, Categories, Podcasts
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    mainBlock = MainBlock.objects.first()
    firstArticle = Articles.objects.filter(id=mainBlock.firstArticle.id)
    secondArticle = Articles.objects.filter(id=mainBlock.secondArticle.id)
    thirdArticle = Articles.objects.filter(id=mainBlock.thirdArticle.id)

    news = UzbNews.objects.all()[:6]

    article1 = Articles.objects.filter(id=mainBlock.article1.id)
    article2 = Articles.objects.filter(id=mainBlock.article2.id)
    article3 = Articles.objects.filter(id=mainBlock.article3.id)
    article4 = Articles.objects.filter(id=mainBlock.article4.id)
    article5 = Articles.objects.filter(id=mainBlock.article5.id)
    article6 = Articles.objects.filter(id=mainBlock.article6.id)
    video = Video.objects.first()
    podcast = Podcasts.objects.get(id=mainBlock.podcast.id)

    article7 = Articles.objects.get(id=mainBlock.article7.id)
    article8 = Articles.objects.get(id=mainBlock.article8.id)
    article9 = Articles.objects.get(id=mainBlock.article9.id)
    article10 = Articles.objects.get(id=mainBlock.article10.id)
    article11 = Articles.objects.get(id=mainBlock.article11.id)
    article12 = Articles.objects.get(id=mainBlock.article12.id)

    tests = Tests.objects.all()[:6]


    bestArticle = Articles.objects.filter(id=mainBlock.bestArticle.id)

    # blockArticles = Articles.objects.all()[:6]

    ticker = Ticker.objects.first()
    return render(request, "main/index.html", {"ticker": ticker,
                                               "firstArticle": firstArticle,
                                               "secondArticle": secondArticle,
                                               "thirdArticle": thirdArticle,
                                               # "mainblock": mainBlock,
                                               # "blockArticles": blockArticles,
                                               "article1": article1,
                                               "article2": article2,
                                               "article3": article3,
                                               "article4": article4,
                                               "article5": article5,
                                               "article6": article6,
                                               "bestArticle": bestArticle,
                                               "article7": article7,
                                               "article8": article8,
                                               "article9": article9,
                                               "article10": article10,
                                               "article11": article11,
                                               "article12": article12,
                                               "news": news,
                                               "video": video,
                                               "tests": tests,
                                               "podcast": podcast,
                                               })


def article_detail(request, slug):
    article = get_object_or_404(Articles, slug=slug)
    # print("#" * 100)
    # print(article.views)
    article.views += 1
    article.save()
    # article.refresh_from_db()

    # print("#" * 100)
    # F()
    # article.views
    # F(article.views) + 1
    # print()
    return render(request, "main/article_detail.html", {"article": article})


def uzb_news_detail(request, id):
    news = get_object_or_404(UzbNews, id=id)
    news.views += 1
    news.save()
    return render(request, "main/news_detail.html", {"news": news})


def world_news_detail(request, id):
    news = get_object_or_404(WorldNews, id=id)
    news.views += 1
    news.save()
    return render(request, "main/news_detail.html", {"news": news})


def tests(request):
    mainBlock = MainBlock.objects.first()

    bestArticle = Articles.objects.get(id=mainBlock.bestArticle.id)

    tests = Tests.objects.all()
    return render(request, "main/tests.html", {"tests": tests, 'article': bestArticle, })


def categories(request):
    page = request.GET.get('page', 1)
    mainBlock = MainBlock.objects.first()
    bestArticle = Articles.objects.get(id=mainBlock.bestArticle.id)
    categories = Categories.objects.all()
    articles = Articles.objects.all()
    tests = Tests.objects.all()
    podcast = Podcasts.objects.get(id=mainBlock.podcast.id)
    paginator = Paginator(articles, 3)
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return render(request, "main/categories.html", {"categories": categories,
                                                    "articles": articles,
                                                    "tests": tests,
                                                    "bestArticle": bestArticle,
                                                    "podcast": podcast,
                                                    "page_obj": page_obj,
                                                    })


def category_view(request, slug):
    page = request.GET.get('page', 1)
    category = get_object_or_404(Categories, url=slug)
    categories_list = Categories.objects.all()
    articles = Articles.objects.filter(categories_id=category.id)
    paginator = Paginator(articles, 3)
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return render(request, "main/category.html", {"category": category,
                                                  "categories": categories_list,
                                                  # "articles": articles,
                                                  "page_obj": page_obj,
                                                  })


def podcasts(request):
    podcasts_list = Podcasts.objects.all()
    return render(request, "main/podcasts.html", {"podcasts": podcasts_list, })


def news(request):
    return render(request, "main/news.html", )