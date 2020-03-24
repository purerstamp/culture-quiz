from django.db import models

# Create your models here.
class Bar(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=50)
  address = models.CharField(max_length=200)
  tel = models.CharField(max_length=10)
  openingTime = models.CharField(max_length=5)
  closingTime = models.CharField(max_length=5)
  openingTime2 = models.CharField(max_length=5)
  closingTime2 = models.CharField(max_length=5)
  website = models.CharField(max_length=200)
  def __str__(self):
    return self.name
