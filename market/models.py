from django.db import models
from django.contrib import admin

class Prices(models.Model):
  currency  = models.CharField(max_length=3)
  day       = models.DecimalField(max_digits=16,decimal_places=2)
  week      = models.DecimalField(max_digits=16,decimal_places=2)
  month     = models.DecimalField(max_digits=16,decimal_places=2)
  timestamp = models.DateTimeField(auto_now=True)

  def __unicode__(s): return "%s < %s >" % (s.currency, s.day)

admin.site.register(Prices)
