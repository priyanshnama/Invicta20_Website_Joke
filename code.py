# root login email dabefot870@oncloud.ws
# root login password Tendua.jr123
# root Refral Code Tendua54
import urllib
import string 
import random 
import time

#fields
firstname = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 5))
email = firstname + "@gmail.com"
lastname = 'Jr'
college = 'IIITDMJ'
city = 'Dumna'
phone = '1234567890'
password = 'dumnarockzz'
refral = 'Tendua54'


data = {
        "firstname" : firstname,
        "lastname"  : lastname,
        "email"     : email,
        "college"   : college,
        "city"      : city,
        "phone"     : phone,
        "password"  : password,
        "refral"    : refral,
       }
       
#encoded_data = urllib.urlencode(data)
#content = urllib2.urlopen("https://invicta20.org/register?action=validate(event)",encoded_data)
