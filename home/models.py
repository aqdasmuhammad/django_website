from django.db import models

# Create your models here.

class Messages(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    message=models.TextField()

    def __str__(self):
        return self.name

class eventregister(models.Model):
    name=models.CharField(max_length=30)
    mtype=models.CharField(max_length=30)
    title=models.CharField(max_length=50)
    ed=models.CharField(max_length=30)
    description=models.TextField()

    def __str__(self):
        return self.name

class complaintfile(models.Model):
    name=models.CharField(max_length=30)
    mtype=models.CharField(max_length=30)
    tname=models.CharField(max_length=50)
    complaint=models.TextField()

    def __str__(self):
        return self.name

class meetingp(models.Model):
    name=models.CharField(max_length=30)
    post=models.CharField(max_length=30)
    tname=models.CharField(max_length=50)
    aud=models.CharField(max_length=50)
    tnd=models.CharField(max_length=50)
    agenda=models.TextField()

    def __str__(self):
        return self.name

class mreport(models.Model):
    name=models.CharField(max_length=30)
    post=models.CharField(max_length=30)
    tname=models.CharField(max_length=50)
    mon=models.CharField(max_length=15)
    report=models.TextField()

    def __str__(self):
        return self.name