from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=92)

    def __str__(self):
        return self.name


class Articles(models.Model):
    title = models.CharField(max_length=192)
    description = models.CharField(max_length=1024)
    md_text = models.TextField()
    posted_on = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} by {self.author}"
