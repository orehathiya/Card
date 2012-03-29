import os
from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    contract_count = models.IntegerField()
    contract_term = models.DateField()
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    call_number = models.CharField(max_length=200)
    fax_number = models.CharField(max_length=200)
    url = models.URLField()
    message = models.TextField()

    def __unicode__(self):
        return self.name

class Meishi(models.Model):
    have_users = models.ManyToManyField(User, blank=True)
    company = models.ForeignKey(Company)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    kana_first_name = models.CharField(max_length=200)
    kana_last_name = models.CharField(max_length=200)
    roma_first_name = models.CharField(max_length=200)
    roma_last_name = models.CharField(max_length=200)
    belong = models.CharField(max_length=200)
    post = models.CharField(max_length=200)
    call_number = models.CharField(max_length=200)
    fax_number = models.CharField(max_length=200)
    mail = models.EmailField()
    url = models.URLField()
    message = models.TextField()
    image = models.ImageField(upload_to=os.path.join(os.path.dirname(__file__), 'images'))

    def __unicode__(self):
        return self.first_name

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    company = models.ForeignKey(Company)
    meishi = models.OneToOneField(Meishi)

    def __unicode__(self):
        return self.user.username

