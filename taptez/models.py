# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from taptez import vendor_utils

# Create your models here.

vehicle_brand = vendor_utils.vehicle_brand()

class VendorProfile(models.Model):
    user = models.ForeignKey(User,null=False, blank=False)
    profile_img = models.TextField(max_length=256)
    district = models.CharField(max_length=2)
    state = models.CharField(max_length=2)
    time = models.DateTimeField(auto_now=True, blank=True)
    modified_time = models.DateTimeField(auto_now=True, blank=True)

class Vehicle(models.Model):
    vendor = models.ForeignKey(VendorProfile,null=False,blank=False)
    brand = models.CharField(max_length=2,choices=vehicle_brand,default='MH')
    model_name = models.CharField(max_length=256,null=False,blank=False)
    model_no = models.CharField(max_length=256,null=False,blank=False)
    max_pass = models.IntegerField(default=0)
    vehicle_image = models.TextField()

