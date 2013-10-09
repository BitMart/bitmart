from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib import admin
from vendor.models import Vendor
from django.template.defaultfilters import slugify
import zlib

class Category(models.Model):
  title  = models.CharField(max_length=64)
  parent = models.ForeignKey('self', null=True, blank=True)
  slug      = models.SlugField()

  def children(self):
    return self.category_set.all()
  sub_cats = property(children)

  def save(self, *a, **kw):
    self.slug = slugify(self.title)
    super(Category, self).save(*a, **kw)

  def __unicode__(self): return self.title


class Listing(models.Model):
  vendor    = models.ForeignKey(Vendor)
  title     = models.CharField(max_length=64)
  slug      = models.SlugField()
  description \
            = models.TextField()
  cost      = models.DecimalField(decimal_places=6,max_digits=6)
  image     = models.FileField(upload_to='listing')
  timestamp = models.DateTimeField(auto_now_add=True)

  def save(self, *a, **kw):
    self.slug = slugify(self.title)
    super(Listing, self).save(*a, **kw)

class ListingForm(ModelForm):
  class Meta:
    model = Listing
    fields = ['title','description','cost','image']

class Purchase(models.Model):
  buyer     = models.ForeignKey(User)
  listing   = models.ForeignKey(Listing)
  status    = models.CharField(max_length=64)
  timestamp = models.DateTimeField(auto_now_add=True)

  def safeid(self): return zlib.crc32(str(self.id))
  safe_id = property(safeid)

class Review(models.Model):
  buyer     = models.ForeignKey(User)
  listing   = models.ForeignKey(Listing)
  content   = models.TextField()
  timestamp = models.DateTimeField(auto_now_add=True)

admin.site.register(Category)
admin.site.register(Listing)
admin.site.register(Purchase)
admin.site.register(Review)
