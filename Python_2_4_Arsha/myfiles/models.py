from django.db import models

# Create your models here.
class Type(models.Model):
    nomi = models.CharField(max_length=20)
    def __str__(self):
        return self.nomi
class Portfolio(models.Model):
    nomi = models.CharField(max_length=40)
    comp_nomi = models.CharField(max_length=40)
    tur = models.ForeignKey(Type,on_delete=models.CASCADE)
    url = models.CharField(max_length=100,null=True,blank=True)
    date = models.DateField()
    text = models.TextField()
    rasm1 = models.ImageField(upload_to='media')
    rasm2 = models.ImageField(upload_to='media',null=True,blank=True)
    rasm3 = models.ImageField(upload_to='media',null=True,blank=True)
class Services(models.Model):
    rasmi = models.ImageField(upload_to='media')
    nomi = models.CharField(max_length=20)
    text = models.TextField()
    sana = models.DateTimeField()
class Team(models.Model):
    ismi = models.CharField(max_length=20,null=True,blank=True)
    familyasi = models.CharField(max_length=20)
    yoshi = models.IntegerField()
    sana = models.DateTimeField()
    text = models.TextField()
    rasmi = models.ImageField(upload_to='media')
class Murojaat(models.Model):
    ism=models.CharField(max_length=20)
    mail=models.EmailField(max_length=20)
    sub=models.CharField(max_length=20)
    text=models.TextField()
    date=models.DateField(auto_now=True)


