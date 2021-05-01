from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.contrib.auth import get_user_model
from taggit.managers import TaggableManager
from PIL import Image

User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=60, blank=False, null=False)
    desc = models.TextField()
    tags = TaggableManager()
    post_img = models.ImageField(upload_to='posts_img', null=True, blank=True)
    date_posted = models.DateField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    deleted = models.BooleanField(blank=False, null=False, default=False)
    slug = models.SlugField(max_length=50, null=True, blank=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        if self.post_img:
            img = Image.open(self.post_img.path)
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.post_img.path)

        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('news-detail', kwargs={'slug': self.slug})

    def __str__(self) -> str:
        return self.title


class ViewCounter(models.Model):
    day = models.IntegerField(unique=True, validators=[MinValueValidator(1),
                                                       MaxValueValidator(30)])
    views = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'Day {self.day} : {self.views} views'
