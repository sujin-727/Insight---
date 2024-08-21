from django.db import models

class Drama(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField()
    thumbnail = models.URLField()
    description = models.TextField()

    def __str__(self):
        return self.title