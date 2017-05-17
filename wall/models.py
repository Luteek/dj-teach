from django.db import models

# Create your models here.

class Post(models.Model):
    caption = models.CharField(max_length=200)
    content = models.CharField(max_length=2000)
    image   = models.URLField()
    pub_date = models.DateTimeField('date published')
