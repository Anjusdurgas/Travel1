from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')#pics is a folder name means where to upload the img
    desc=models.TextField()

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')  # pics is a folder name means where to upload the img
    desc = models.TextField()

    def __str__(self):
        return self.name  #to view the name that we given in the admin panel for a parti. image