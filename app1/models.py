from django.db import models

# Create your models here.
class Students(models.Model):
    rn = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    addr = models.CharField(max_length=200)
    marks = models.FloatField()
    email = models.EmailField()

    def __str__(self):
        return self.name