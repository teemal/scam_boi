import requests
import os
import random
import string
import json

url = "https://eslplaygames.com/openid/ZMR38yLzJbGUWBg65BLhL4BP"

chars = string.ascii_letters + string.digits + '^%$!()'
random.seed = (os.urandom(1024))

n = open('names.txt', "r")
for name in n:
    names = name.split()
    for i in names:
       for j in names:
           for k in names:
                name_boi = name.split(",")
                uname = name_boi[0].lower() + str(random.randint(3,99))
                pass_boi = ''.join(random.choice(chars) for i in range(5))

                requests.post(url, allow_redirects=False, data={
                    'username': uname,
                    'password': pass_boi
                })

                print(("username: {0} \npassword: {1} \n").format(uname, pass_boi))
