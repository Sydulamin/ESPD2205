from django.db import models


# Create your models here.

class Profile(models.Model):
    Name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=6)
    image = models.ImageField(upload_to='prof_pic/' ,  default='default/default.png', blank=True, null=True)
    phone = models.PositiveIntegerField()
    address = models.TextField(max_length=200)

    def __str__(self):
        return str(self.Name)
