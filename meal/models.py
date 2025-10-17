from django.db import models

# Create your models here.

class Taom(models.Model):
    nomi = models.CharField(max_length=50)
    tavsifi = models.TextField()
    narxi = models.IntegerField()
    mavjudligi = models.BooleanField()
    kategoriyasi = models.CharField(choices=[("salat", "Salat"), ("asasiy", "Asasiy taollar"), ("shirinliklar", "Shirinliklar")])
    rasm = models.ImageField()
    
    def __str__(self):
        return self.nomi
    
     
       