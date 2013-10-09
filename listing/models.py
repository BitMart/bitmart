from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

class Category(models.Model):
  title  = models.CharField(max_length=64)
  parent = models.ForeignKey('self', null=True, blank=True)
  def __unicode__(self): return self.title

  def children(self):
    return self.category_set.all()
  sub_cats = property(children)

class Listing(models.Model):
  vendor    = models.ForeignKey(User)
  title     = models.CharField(max_length=64)
  cost      = models.DecimalField(decimal_places=6,max_digits=6)
  img_uri   = models.CharField(max_length=32)
  timestamp = models.DateTimeField(auto_now_add=True)

class Purchase(models.Model):
  buyer     = models.ForeignKey(User)
  timestamp = models.DateTimeField(auto_now_add=True)
  status    = models.CharField(max_length=64)

class Review(models.Model):
  buyer     = models.ForeignKey(User)
  content   = models.TextField()
  timestamp = models.DateTimeField(auto_now_add=True)

admin.site.register(Category)
admin.site.register(Listing)
admin.site.register(Purchase)
admin.site.register(Review)
