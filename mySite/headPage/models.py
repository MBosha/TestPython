from django.db import models
from django.contrib.auth.models import User

class Section(models.Model):
    class Meta:
        db_table = "section"
 
    section_title = models.CharField(max_length=200, default='DEFAULT')
    section_url = models.CharField(max_length=50)
    section_description = models.TextField()
 
    def title(self):
        return self.section_title

class Article(models.Model):
    class Meta:
        db_table = "article"
 
    article_title = models.CharField(max_length=200)
    article_section = models.ForeignKey(Section, on_delete=models.CASCADE,)
    article_author = models.ForeignKey(User, on_delete=models.CASCADE,)
    article_date = models.DateTimeField('Дата публикации')
    article_content = models.TextField()
    article_status = models.IntegerField()
 
    def title(self):
        return self.article_title

class Book(models.Model):
    header = models.CharField(max_length=200, help_text='Заголовок', blank=False,)
    description = models.TextField(help_text='Описание', blank=False,)

class Tovar(models.Model):
    class Meta:
        db_table = "tovar"
    
    name = models.CharField(max_length=200)
    discript = models.TextField()
    cost = models.IntegerField()

class MyMenu(models.Model):
    class Meta:
        db_table = "mymenu"
        ordering = ["l1"]

    l1 = models.DecimalField(max_digits=3, decimal_places=0)
    l2 = models.DecimalField(max_digits=3, decimal_places=0)
    l3 = models.DecimalField(max_digits=3, decimal_places=0)
    l4 = models.DecimalField(max_digits=3, decimal_places=0)
    l5 = models.DecimalField(max_digits=3, decimal_places=0)
    first = models.BooleanField()
    visible = models.BooleanField()
    content = models.CharField(max_length=200)
    level = models.DecimalField(max_digits=3, decimal_places=0)
    link = models.CharField(max_length=200)
    activ = models.BooleanField()