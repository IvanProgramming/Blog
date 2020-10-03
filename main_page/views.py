from django.shortcuts import render, redirect

from .models import Articles, Category
import random


# TODO - Add pagination


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


def show_category(request, cat_id):
    cat_obj = Category.objects.get(id=cat_id)
    return render(request, "category.html", context={
        "cat_articles": Articles.objects.filter(category=cat_obj),
        "articles": Articles.objects.all(),
        "categories": Category.objects.all(),
        "category": Category.objects.get(id=cat_id)
    })


def show_contacts(request):
    return render(request, "contact.html")


def show_about(request):
    return render(request, "about.html")
