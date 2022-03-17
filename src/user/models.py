from django.db import models

# Create your models here.
class User(models.Model):
    # id = models.AutoField(primary_key=True) -> default
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
