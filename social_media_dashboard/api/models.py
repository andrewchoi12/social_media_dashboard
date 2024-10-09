from django.db import models

# Create your models here.

class SocialMediaPost(models.Model):
    platform = models.CharField(max_length=50)
    post_id = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    shares = models.IntegerField(default=0)
    timestamp = models.DateTimeField()
    sentiment_score = models.FloatField()

    def __str__(self):
        return f"{self.platform} Post: {self.post_id}"