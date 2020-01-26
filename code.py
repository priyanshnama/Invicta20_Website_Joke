# root login email dabefot870@oncloud.ws
# root login password Tendua.jr123
# root Refral Code Tendua54

import string
import urllib3
import random
import json


# log file
log = open("log.txt", "a+")
Head = ["firstname\t", "lastname\t", "email\t\t\t", "college\t", "city\t", "phone\t\t", "password\t", "refral\t"]
log.writelines(Head)

code = input("Enter Your Refral code: ")
points = int((int(input("how much point you want to generate: ")))/10)
point = int(points/10)
# fields
for i in range(point):
    firstname = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    email = firstname + "@gmail.com"
    lastname = 'Jr'
    college = 'IIITDMJ'
    city = 'Dumna'
    phone = '1234567890'
    password = 'dumnarockzz'
    refral = code

    data = {
        "firstname": firstname,
        "lastname": lastname,
        "email": email,
        "college": college,
        "city": city,
        "phone": phone,
        "password": password,
        "refral": refral,
    }
    L = [v for k, v in data.items()]
    L[0] = "    " + L[0]
    L[1] = "      " + L[1]
    for index in range(len(L)):
        L[index] = L[index] + "\t"
    log.writelines("\n")
    log.writelines(L)

    http = urllib3.PoolManager()
    try:
        r = http.request('GET', 'https://invicta20.org/register', retries=False)
        encoded_data = json.dumps(data).encode('utf-8')
        r = http.request('POST', 'https://invicta20.org/register', body=encoded_data,
                         headers={'Content-Type': 'application/json'})
        json.loads(r.data.decode('utf-8'))['json']
        var = {'attribute': 'value'}
    except urllib3.exceptions.NewConnectionError:
        print('Connection failed.')
    except json.decoder.JSONDecodeError:
        var = {'attribute': 'value'}
