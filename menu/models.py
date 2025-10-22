from django.db import models

# Create your models here.
class Taom(models.Model):
    nomi = models.CharField(max_length=50)
    tavsifi = models.TextField()
    narxi = models.DecimalField(max_digits=10,decimal_places=2)
    mavjudligi = models.CharField(choices=[
        ('Ha','Ha'),
        ('Yoq','Yoq')
    ],default='Ha')
    kategoriyasi = models.CharField(choices=[
        ('Salatlar','Salatlar'),
        ('Asosiy taomlar','Asosiy taomlar'),
        ('Shirinliklar','Shirinliklar'),
        ('Ichimliklar','Ichimliklar')
    ])
    image = models.ImageField(upload_to='image', blank=True, null=True)
    
    def __str__(self):
        return self.nomi
    
     
       