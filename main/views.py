from django.shortcuts import render, get_object_or_404
from .models import Ticker, MainBlock, Articles, UzbNews, Video, Tests, WorldNews, Categories, Podcasts
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import random
from datetime import datetime, timedelta
from django.views import View
from django.http import JsonResponse
from . import my_date


def index(request):
    mainBlock = MainBlock.objects.first()
    firstArticle = Articles.objects.filter(id=mainBlock.firstArticle.id)
    secondArticle = Articles.objects.filter(id=mainBlock.secondArticle.id)
    thirdArticle = Articles.objects.filter(id=mainBlock.thirdArticle.id)
    now = datetime.now()
    before = now - timedelta(weeks=1)
    news = UzbNews.objects.filter(date_created__gte=str(before.date()))
    try:
        news = random.choices(news, k=6)
    except:
        news = []

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
    rand_article = Articles.objects.all()[:20]
    rand_article = random.choices(rand_article, k=2)
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
    return render(request, "main/article_detail.html", {"article": article,
                                                        "rand_article": rand_article,
                                                        })


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
    articles = Articles.objects.all()[:2]
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
    articles = Articles.objects.filter(categories_id=category.id)[:2]
    paginator = Paginator(articles, 3)
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return render(request, "main/category.html", {"category": category,
                                                  "categories": categories_list,
                                                  "articles": articles,
                                                  "page_obj": page_obj,
                                                  })


def podcasts(request):
    podcasts_list = Podcasts.objects.all()
    return render(request, "main/podcasts.html", {"podcasts": podcasts_list, })


def news(request):
    main_news = WorldNews.objects.all()[:1]
    main_news = random.choice(main_news)
    uzb_news3 = UzbNews.objects.all()[:3]
    uzb_news2 = UzbNews.objects.all()[3:6]
    return render(request, "main/news.html", {"main_news": main_news,
                                              "uzb_news3": uzb_news3,
                                              "uzb_news2": uzb_news2,
                                              })


def dynamic_category(request, *args, **kwargs):
    print("\n***********************************************************************", request.method)
    last_date = request.GET.get('seeMoreCategory')
    categoryId = int(request.GET.get('categoryId'))
    # print("\n***********************************************************************", categoryId)
    date_filter = datetime.strptime(last_date, "%Y-%m-%d %H:%M:%S")
    articles = Articles.objects.filter(date_created__lte=date_filter, categories_id=categoryId).order_by('-date_created')[:2]
    data = []
    if "/ru/" in request.path:
        lang_link = "/ru/"
    else:
        lang_link = "/uz"
    if not articles:
        return JsonResponse({'data': False})
    for article in articles:
        obj = {
            "id": article.id,
            "date_for": article.date_created.strftime("%Y-%m-%d %H:%M:%S"),
            "image": article.image.url,
            "date_created": my_date.my_month_ru(article.date_created) if "/ru/" in request.path else my_date.my_month_uz(article.date_created),
            "article_detail": lang_link + "article_detail/" + article.slug,
            "title": article.title,
            "short_description": article.short_description,
            "category": article.categories.name,
            "cat-id": article.categories_id,
        }
        data.append(obj)
    data[-1]['last-article'] = True
    print(data)

    # print(articles)
    # print(last_date)
    # my = datetime.now()
    # print(my.strftime("%Y-%m-%d %H:%M:%S"))
    return JsonResponse({'data': data})



class DynamicArticles(View):
    def get(self, request, *args, **kwargs):
        last_article_id = request.GET.get('seeMoreCategories')
        articles = Articles.objects.filter(pk__lt=int(last_article_id))[:2]
        data = []
        if "/ru/" in request.path:
            lang_link = "/ru/"
        else:
            lang_link = "/uz"
        # print("**********************************************************", request.path)
        if not articles:
            return JsonResponse({'data': False})
        for article in articles:
            obj = {
                'id': article.id,
                'title': article.title,
                'image': article.image.url,
                # 'date_created': article.date_created.strftime("%d %B %Y"),
                'date_created': my_date.my_month_ru(article.date_created) if "/ru/" in request.path else my_date.my_month_uz(article.date_created),
                'slug': lang_link + "article_detail/" + article.slug,
                'short_description': article.short_description,
                'category': article.categories.name,
                'category_url': lang_link + "category/" + article.categories.url,
            }
            data.append(obj)
        data[-1]['last-article'] = True
        # print("**************", data)
        return JsonResponse({'data': data})





