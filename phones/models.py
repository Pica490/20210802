from django.db import models
from django.utils.text import slugify


class Phone(models.Model):

    name = models.CharField(max_length=40)
    price = models.TextField(max_length=1000)
    image = models.ImageField()
    release_date = models.DateField()
    lte_exist = models.BooleanField()
    slug = models.SlugField(max_length=40)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Phone, self).save(*args, **kwargs)