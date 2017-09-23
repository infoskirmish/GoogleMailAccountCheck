#!/usr/bin/env python3

# Credit: Idea and motivation inspired by X0rz's blog post:
# https://blog.0day.rocks/abusing-gmail-to-get-previously-unlisted-e-mail-addresses-41544b62b2T
# Enjoy!

import requests

with open("names") as f:
    content = f.readlines()

for name in content:
    name = name[:-1]
    response = requests.get("https://mail.google.com/mail/gxlu?email=" + name)

    if 'Set-Cookie' in response.headers:
        print("["+ name + "] Found")
    else:
        print("["+ name + "] NOT found")
