from django.db import models
from bars.models import Bar

# Create your models here.
class Event(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=100)
  type = models.CharField(max_length=50)
  day = models.CharField(max_length=8)
  time = models.CharField(max_length=5)
  location = models.ForeignKey(Bar, on_delete=models.DO_NOTHING)
  cqview = models.CharField(max_length=500, default='On vous concocte ça le plus rapidement possible.. avec modération tout de même ;p')
  def __str__(self):
    return self.name
