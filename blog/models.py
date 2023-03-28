from django.db import models

class Kakugodno(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    price = models.IntegerField()
    created = models.DateTimeField()

    def __str__(self) -> str:
        return self.title