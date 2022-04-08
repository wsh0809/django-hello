from django.db import models
from datetime import datetime
# Create your models here.

class BaseModel(models.Model):
    create_time = models.DateTimeField(default=datetime.now)

    class Meta:
        abstract = True
        ordering = ['name']


class Article(models.Model):
    id = models.BigAutoField(primary_key=True)
    author = models.CharField(max_length=50)
    create_time = models.DateTimeField(default=datetime.now)
    content = models.CharField(max_length=10000)
    title = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.title if self.title else ''

class Category(BaseModel):
    name = models.CharField(max_length=50)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.name

class ArticleCategoryShip(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    date_joined = models.DateTimeField()

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True)
    link = models.CharField(max_length=200)
    content = models.CharField(max_length=1000)