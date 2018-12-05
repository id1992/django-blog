from django.db import models
from django.utils import timezone

class Post(models.Model):
    # Django2 변경사항
    # TypeError: __init__() missing 1 required positional argument: 'on_delete'
    # Django2부터는 on_delete 아규먼트가 필요
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
