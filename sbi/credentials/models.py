from django.db import models
from django.db.models.deletion import CASCADE

class District(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Branch(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name



class Forum(models.Model):
    name = models.CharField(max_length=250)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=250)
    phone = models.BigIntegerField()
    mailid = models.TextField()
    address = models.TextField()
    account = models.CharField(max_length=250)

    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
