from django.db import models
from django.urls import reverse

from embed_video.fields import EmbedVideoField

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date']


class Author(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)

    def __str__(self):
        return self.name + ' ' + self.surname

class Note(models.Model):
    content = models.TextField()

class Video(models.Model):
    title = models.CharField(max_length=100, null=True)
    url = EmbedVideoField()

    def __str__(self):
        return str(self.title)

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add = True)
    tags = models.ManyToManyField(Tag)
    image = models.ImageField(upload_to = 'images/', blank=True)
    videos = models.ManyToManyField(Video, blank=True)
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article:detail',kwargs={'slug':self.slug})

    class Meta:
        ordering = ['-date']

