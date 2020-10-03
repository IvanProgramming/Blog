from django.contrib import admin
from django.urls import path

from main_page.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_main_page),
    path('post/<slug:article_name>', show_article),
    path('random', show_random),
    path('category/<int:cat_id>', show_category),
    path('about', show_about),
    path('contacts', show_contacts)
]
