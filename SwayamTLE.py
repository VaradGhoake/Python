import urllib
from bs4 import BeautifulSoup

req = urllib.urlopen("http://www.n2yo.com/satellite/?s=41607#results")
html = BeautifulSoup(req, 'html')

for tle in html.findAll('pre'):
    tle = tle.text
    print tle
