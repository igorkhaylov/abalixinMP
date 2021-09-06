from django.shortcuts import render, get_object_or_404
from .models import Ticker, MainBlock, Articles


def index(request):
    mainBlock = MainBlock.objects.first()
    firstArticle = Articles.objects.filter(id=mainBlock.firstArticle.id)
    secondArticle = Articles.objects.filter(id=mainBlock.secondArticle.id)
    thirdArticle = Articles.objects.filter(id=mainBlock.thirdArticle.id)
    blockArticles = Articles.objects.all()[:6]


    ticker = Ticker.objects.first()
    return render(request, "main/index.html", {"ticker": ticker,
                                               "firstArticle": firstArticle,
                                               "secondArticle": secondArticle,
                                               "thirdArticle": thirdArticle,
                                               # "mainblock": mainBlock,
                                               "blockArticles": blockArticles,
                                               })


def article_detail(request, slug):
    article = get_object_or_404(Articles, slug=slug)
    return render(request, "main/article_detail.html", {"article": article})
