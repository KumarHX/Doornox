import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
from datetime import datetime


'''
Models must be backwards compatible with all api versions.

'''

'''
Note every model we register (including the django User model) can support upto ~4 billion instances
since the built in id is int(11)
http://stackoverflow.com/questions/2672975/django-biginteger-auto-increment-field-a-primary-key
so be wary while scaling
'''

class Userinfo(models.Model):
    fname = models.TextField()
    lname = models.TextField()
    email = models.TextField()
    fbid = models.CharField(max_length=20, blank=True)
    lnkdid = models.CharField(max_length=20, blank=True)
    gid = models.CharField(max_length=20, blank=True)
    goog_img_url = models.TextField(default='', blank=True)
    location = models.TextField(blank=True)
    work_location = models.TextField(blank=True)
    company = models.TextField(blank=True)
    job_title = models.TextField(blank=True)
    funny_saying = models.TextField(blank=True)
    resume_link = models.TextField(blank=True)
    lnkd_pubprofile = models.TextField(default='', blank=True)
    lnkd_img_url = models.TextField(default='', blank=True)
    last_login = models.DateTimeField(default=datetime.now()) #when user has last logged ins
    datetime = models.DateTimeField(default=datetime.now()) #when user is first created 
    num_logins = models.IntegerField(null=True, blank=True) #number of times user logs in
    def __unicode__ (self): # __str__ on Python 3
        return str(self.fname + ' ' + self.lname + ' (' + self.email + ')')

class Job(models.Model):
    poster = models.ForeignKey('Userinfo')
    company_name = models.TextField(blank=True)
    location = models.TextField(blank=True)
    job_title = models.TextField(blank=True)
    job_description = models.TextField(blank=True)
    salary_min = models.IntegerField(null=True, blank=True)
    salary_max = models.IntegerField(null=True, blank=True)
    career_level = models.IntegerField(default=3) # 0 = low, 1 = mid, 2 = high, 3 n/a
    company_link = models.TextField(blank=True)
    glassdoor_link = models.TextField(blank=True)
    additional_comments = models.TextField(default='', blank=True)
    datetime = models.DateTimeField(default=datetime.now())

class Message(models.Model): # INBOX FEATURE
    _from = models.ForeignKey('Userinfo', related_name='from_user')
    _to = models.ForeignKey('Userinfo', related_name='to_user')
    to_email = models.TextField()
    message = models.TextField()
    content = models.TextField()
    read = models.BooleanField(default=False)
    datetime = models.DateTimeField(default=datetime.now())
    attachment_path = models.TextField(default='')

class Recommendation(models.Model):
    recommender = models.ForeignKey('Userinfo', related_name='recommender_user')
    recommendee = models.ForeignKey('Userinfo', related_name='recommendee_user')
    receiver = models.ForeignKey('Userinfo')
    receiver_email = models.TextField()
    preference = models.IntegerField() # 0 = diamond, 1 = gold, 2 = silver = models.TextField()
    cover_letter_link = models.TextField()

class Friendship(models.Model): # RELATIONSHIP BETWEEN USERS
    user_1 = models.ForeignKey('Userinfo', related_name='user_1_user')
    user_2 = models.ForeignKey('Userinfo', related_name='user_2_user')

class Starred(models.Model):
    job = models.ForeignKey('Job')
    user = models.ForeignKey('Userinfo')

class ContactUsMsg(models.Model):
    name = models.TextField()
    email = models.TextField()
    content = models.TextField()

class SearchTerm(models.Model):
    term = models.TextField()
    num_results = models.IntegerField()
    searcher = models.ForeignKey('Userinfo', null=True)
    date = models.DateTimeField()
