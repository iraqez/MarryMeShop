from django.db import models
from django.db.models import permalink
from gallery.fileds import ThumbnailImageField

class Item(models.Model):
    pass


    @permalink
    def get_absolute_url(self):
        return ('item_detail', None, {'object_id': self.id})

class Photo(models.Model):
    item = models.ForeignKey(Item)
    title = models.CharField(verbose_name=r"Название", max_length=100)
    image = ThumbnailImageField(verbose_name=r"Фото", upload_to='media/images/main')
    caption = models.CharField(verbose_name=r"Описание", max_length=250, blank=True)

    class Meta:
        ordering = ['title']
        verbose_name = r"Фотография"
        verbose_name_plural = r"Фотографии"

    def __str__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return ('photo_detail', None, {'object_id': self.id})

