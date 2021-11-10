from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class PublishedArticleManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='created')


class Article(models.Model):
    STATUS = (
        ("draft", "Draft"),
        ("created", "Created"),
    )
    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120, unique=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = RichTextUploadingField(null=True, blank=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS, default="draft")
    objects = models.Manager()
    published = PublishedArticleManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:get_article', args=[self.id, self.slug])
