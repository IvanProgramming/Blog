from django.shortcuts import render, redirect

from .models import Articles, Category
import random


def show_main_page(request):
    return render(request, "index.html", context={
        "articles": Articles.objects.all(),
        "categories": Category.objects.all()
    })


def show_article(request, article_name):
    return render(request, "post.html", context={
        "article": Articles.objects.get(id=article_name)
    })


def show_random(request):
    r_article = random.choice(Articles.objects.all())
    return redirect(f"/post/{r_article.id}")
