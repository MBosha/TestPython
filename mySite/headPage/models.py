from django.db import models
from django.contrib.auth.models import User

class Section(models.Model):
    class Meta:
        db_table = "section"
 
    section_title = models.CharField(max_length=200, default='DEFAULT')
    section_url = models.CharField(max_length=50)
    section_description = models.TextField()
 
    def __str__(self):
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
 
    def __str__(self):
        return self.article_title
#empty