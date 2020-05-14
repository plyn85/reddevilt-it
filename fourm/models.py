from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# creating post model


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # returning user to post detail page after thr have made a post
        return reverse('post-detail', kwargs={'pk': self.pk})
    # counting the posts of each user

    def count_posts_of(user):
        return Post.objects.filter(author=user).count()
