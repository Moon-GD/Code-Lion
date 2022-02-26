from django.db import models

class Blog(models.Model):
    author = models.CharField(max_length=50)
    body = models.TextField()

    def __str__(self):
        return 'posted by ' + self.author

class Comment(models.Model):
    author = models.CharField(max_length=30)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.body

    def get_date(self):
        char_date = str(self.date)
        return 'Time : ' + char_date[5:7] + '/' + char_date[8:10]