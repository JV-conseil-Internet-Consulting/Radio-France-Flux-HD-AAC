# coding=utf8
# pip3 install requests

import json
import requests
import re

regex = r"(?P<link>http[^,\"]*?/(?P<title>[^\.]*?)\-hifi\.aac\?id=radiofrance)"

pages = [
    "https://www.francemusique.fr",
    "https://www.franceculture.fr",
    "https://www.franceinter.fr",
    "https://www.fip.fr",
]

links = {}

for p in pages:
    try:
        response = requests.get(p)
        result = re.findall(regex, response.text, 0)
        links.update({y: x for x, y in result})
    except Exception as e:
        print(e)

print(json.dumps(links, indent=1, ensure_ascii=False))
