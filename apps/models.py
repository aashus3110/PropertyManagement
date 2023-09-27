from django.db import models

# Create your models here.


class Company(models.Model):
    image = models.ImageField(upload_to="")
    Company_name = models.CharField(max_length=150)
    Location = models.CharField(max_length=150)
    value = models.CharField(max_length=100)
    Company_detail = models.TextField()
    Phone = models.CharField(max_length=13)
    Email = models.CharField(max_length=100)

    def __str__(self):
        return self.Company_name



class Property(models.Model):
    image = models.ImageField(upload_to="media")
    Name = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    type = models.CharField(max_length=150)
    Relation = models.CharField(max_length=150)
    value = models.CharField(max_length=100)
    detail = models.TextField()
    Phone = models.CharField(max_length=13)

    def __str__(self):
        return self.Name
