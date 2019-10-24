from django.db import models


class News(models.Model):
    news_text = models.TextField(max_length=5000)
    pub_date = models.DateTimeField('date published')
