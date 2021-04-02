from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from taggit.managers import TaggableManager


class Post(models.Model):
    title = models.CharField(max_length=60, blank=False, null=False)
    intro_desc = models.TextField(max_length=120, blank=True)
    desc = models.TextField()
    tags = TaggableManager()
    deleted = models.BooleanField(blank=False, null=False, default=False)

    def save(self, *args, **kwargs):
        self.intro_desc = self.desc[:110] + '...'
        super(Post, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title


class ViewCounter(models.Model):
    day = models.IntegerField(unique=True, validators=[MinValueValidator(1),
                                                       MaxValueValidator(30)])
    views = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'Day {self.day} : {self.views} views'
