from django.db import models
from django.db.models import permalink
#from gallery.items.fields import ThumbnailImageField
from PIL import Image

class Item(models.Model):
    pass


    @permalink
    def get_absolute_url(self):
        return ('item_detail', None, {'object_id': self.id})
#
class Photo(models.Model):
    item = models.ForeignKey(Item)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/images/main')
    caption = models.CharField(max_length=250, blank=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return ('photo_detail', None, {'object_id': self.id})
