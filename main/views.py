from django.shortcuts import render, get_object_or_404
from .models import Ticker, MainBlock, Articles, UzbNews, Video, Tests


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


