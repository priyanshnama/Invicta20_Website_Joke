# root login email dabefot870@oncloud.ws
# root login password Tendua.jr123
# root Refral Code Tendua54
import urllib
import urllib2
import requests
import string 
import random 
import time
from bs4 import BeautifulSoup

# getting temp email
res = ''.join(random.choices(string.ascii_uppercase + string.digits, k = N))


data = {
        "firstname" : firstname
        "lastname"  : lastname
        "email"     : email
        "college"   : college
        "city"      : city
        "phone"     : phone
        "password"  : password
        "refral"    : refral
       }
encoded_data = urllib.urlencode(data)
content = urllib2.urlopen("https://invicta20.org/register?action=validate(event)",
        encoded_data)
