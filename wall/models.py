from django.utils import timezone
from django.db import models

# Create your models here.

class Post(models.Model):
    caption = models.CharField(max_length=200)
    content = models.CharField(max_length=2000)
    image   = models.URLField()
    pub_date = models.DateTimeField('date published')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title