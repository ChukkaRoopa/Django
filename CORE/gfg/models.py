from django.db import models

# Create your models here.

class GeeksModel(models.Model):
    title = models.CharField(max_length=100)
    descript = models.TextField()
    image = models.ImageField(upload_to="gfgs", null=True, blank=True)
    id_no = models.IntegerField(null=True, blank=True)