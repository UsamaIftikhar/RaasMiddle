from django.db import models
from django import forms
# Create your models here.
from django.forms import widgets


class userInfo(models.Model):

    # firstName = models.CharField(max_length=100)
    # lastName = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=15)

    # image = models.ImageField(upload_to='pics')
    # address = models.TextField(max_length=40)
    # phoneNumber = models.CharField(max_length=11)
class addapps(models.Model):

    # firstName = models.CharField(max_length=100)
    # lastName = models.CharField(max_length=100)
    import uuid
    # app_id=models.UUIDField(default=uuid.uuid4, primary_key=True)

    app_id=models.UUIDField(primary_key=True)
    appname = models.CharField(max_length=15)
    webaddress = models.CharField(max_length=15)
    user_id = models.ForeignKey(userInfo, on_delete=models.CASCADE)

class company(models.Model):

    company_id=models.UUIDField(primary_key=True)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=15)

class APP(models.Model):


    app_id=models.UUIDField(primary_key=True)
    appname = models.CharField(max_length=15)
    webaddress = models.CharField(max_length=15)
    company_id = models.ForeignKey(company, on_delete=models.CASCADE)


class Keys(models.Model):
    key_id=models.UUIDField(primary_key=True)
