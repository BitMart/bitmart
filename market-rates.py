import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bitmart.settings')

from market.models import Prices

## Fetch code
import urllib2
import json
import time

cache_mins = 20
uri = 'http://api.bitcoincharts.com/v1/weighted_prices.json'
cachef = './weighted_prices.json'

def age_in_mins(filen):
  if not os.path.exists(filen): return 9999

  st = os.stat(filen)
  now = time.mktime(time.localtime())
  return (now - st.st_mtime) / 60

def write_cache(dat):
  cache = open(cachef, 'w')
  cache.write(dat)
  cache.close()

def dl_prices():
  data = urllib2.urlopen(uri).read()
  write_cache(data)
  return data

def read_cache():
  c = open(cachef, 'r')
  return "".join(c.readlines())

def get_prices():
  if age_in_mins(cachef) > cache_mins:
    print "Downloaded"
    d = dl_prices()
  else:
    print "Cached"
    d = read_cache()
  return json.loads(d)

def insert_prices(p):
  all = Prices.objects.all()
  [Prices.delete(_p) for _p in all]

  for k in p:
    if k != 'timestamp':
      Prices(currency=k,day=p[k]['24h'],week=p[k]['7d'],month=p[k]['30d']).save()

insert_prices(get_prices())
