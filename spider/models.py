from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title

class Article(models.Model):
    id = models.BigAutoField(primary_key=True)
    author = models.CharField(max_length=50)
    create_time = models.DateTimeField
    categorys = models.ManyToManyField(Category, through='ArticleCategoryShip')
    content = models.CharField(max_length=10000)

class ArticleCategoryShip(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    date_joined = models.DateTimeField()

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True)
    link = models.CharField(max_length=200)
    content = models.CharField(max_length=1000)