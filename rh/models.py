from django.db import models


class Ganhos(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    price = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.name} {self.price}"

# Create your models here.
