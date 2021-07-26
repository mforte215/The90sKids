from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.utils.text import slugify
from ckeditor.fields import RichTextField
import uuid


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Article(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        User, on_delete=CASCADE, related_name="editorals")
    published_date = models.DateTimeField(auto_now_add=True, editable=False)
    snippet = models.CharField(max_length=250)
    text = RichTextField()
    slug = models.SlugField(unique=True, db_index=True, blank=True)
    tags = models.ManyToManyField(Tag)
    image = models.ImageField(upload_to="editorals", null=True)
    top_post = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True, editable=False, null=True)

    def __str__(self):
        return f"{self.title} by {self.author}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)
