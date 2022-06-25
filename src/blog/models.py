from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from unidecode import unidecode

from embed_video.fields import EmbedVideoField

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date']

class Note(models.Model):
    content = models.TextField()

class Author(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, blank=True, editable=False)

    def __str__(self):
        return self.name + ' ' + self.surname

    def get_absolute_url(self):
        return reverse('author:detail_author',kwargs={'slug':self.slug})

    def save(self, *args, **kwargs):
        if not self.id: # if this is a new item
            newslug = '{0} {1}'.format(self.name, self.surname)
            self.slug = slugify(unidecode(newslug))
        super(Author, self).save(*args, **kwargs)

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
    slug = models.SlugField(max_length=255, blank=True, editable=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article:detail',kwargs={'slug':self.slug})

    def save(self, *args, **kwargs):
        if not self.id: # if this is a new item
            newslug = '{0} {1}'.format(self.title, self.author)
            self.slug = slugify(unidecode(newslug))
        super(Article, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-date']

