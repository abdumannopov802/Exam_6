from django.db import models
from django.utils.html import mark_safe

# Create your models here.

class ContentManager(models.Model):
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=250)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="50" height="50" />' % (self.image))
    image_tag.short_description = 'Image'

    def __str__(self) -> str:
        return self.title


