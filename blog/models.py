from django.db import models

# Create your models here.
class Article(models.Model):
    class Meta:
        db_table = "Articles"

    title = models.CharField(max_length=256, default='')
    category = models.CharField(max_length=256, default='')
    comment = models.CharField(max_length=256, default='')

class Category(models.Model):
    class Meta:
        db_table = "Categorys"

    name = models.CharField(max_length=256, default='')
    explanation = models.CharField(max_length=256, default='')