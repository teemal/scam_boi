import requests
import os
import random
import string
import json

url = "https://eslplaygames.com/openid/ZMR38yLzJbGUWBg65BLhL4BP"

chars = string.ascii_letters + string.digits + '^%$!()'
random.seed = (os.urandom(1024))

names = json.loads(open('names.json')).read()
for name in names:
    for i in names:
        extra = ''.join(random.choice(string.digits))

        uname = name.lower() + extra
        pass_boi = ''.join(random.choice(chars) for i in range(5))

        requests.post(url, allow_redirects=False, data={
            "username": uname,
            "password": pass_boi
        })

        print(("username: {0} \npassword: {1} \n").format(uname, pass_boi))
