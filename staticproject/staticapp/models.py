from django.db import models

# Create your models here.
class A(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='folder')
    desc=models.TextField()
    def __str__(self):
        return self.name
class new(models.Model):
    a=models.CharField(max_length=200)
    b=models.TextField()
    c= models.ImageField(upload_to='folder')
    def __str__(self):
        return self.a


