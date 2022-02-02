from django.db import models

from account.models import User


class Category(models.Model):
    slug = models.SlugField(primary_key=True, max_length=50)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='categories', blank=True, null=True)
    parent = models.ForeignKey('self', related_name='children', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        if self.parent:
            return f'{self.parent} -> {self.name}'
        return self.name


class Build(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    build_time = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='buildings')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='buildings')
    created = models.DateTimeField()

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(upload_to='buildings')
    building = models.ForeignKey(Build, on_delete=models.CASCADE, related_name='images')