from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.query import QuerySet
from django.utils import timezone

def user_directory_path(instance, filename):
    if instance.id is not None:
        return 'auctions/{0}/{1}'.format(instance.id, filename)
    else:
        # Handle the case where instance.id is None (e.g., post not saved yet)
        # You can generate a unique filename or use a default path
        return 'auctions/default/{0}'.format(filename)


class User(AbstractUser):
    pass


class Auction(models.Model):

    class NewManager(models.Manager):
        def get_queryset(self) -> QuerySet:
            return super().get_queryset() .filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=250)
    excerpt = models.TextField(null=True)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    publish = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    start_bid = models.IntegerField(default=0)
    finish_bid = models.IntegerField(default=0)
    status = models.CharField(max_length=10, choices=options, default='draft')
    image = models.ImageField(
        upload_to=user_directory_path)
    objects = models.Manager()
    newmanager = NewManager()

    

    class Meta:
        ordering = ('-publish',)