from django.db import models

class Blog(models.Model):
    author = models.CharField(max_length=50)
    body = models.TextField()

    def __str__(self):
        return 'posted by ' + self.author