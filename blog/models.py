from django.db import models
class leksiya(models.Model):
    nomi = models.CharField(max_length=200)
    rasm = models.ImageField(upload_to='rasm/images')
    text = models.TextField()
    narxi = models.IntegerField()


    def __str__(self):
        return self.nomi
# Create your models here.
class Rasmlar(models.Model):
    rasm = models.ImageField(upload_to='rasm/images')
    text = models.TextField()
    narxi = models.IntegerField()


    def __str__(self):
        return self.text


class Email(models.Model):
    email = models.CharField(max_length=222)
    text = models.TextField()
    subject = models.CharField(max_length=777)
    ismi = models.CharField(max_length=300)

    def __str__(self):
        return self.ismi