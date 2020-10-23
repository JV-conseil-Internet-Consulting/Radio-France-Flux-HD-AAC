#!/usr/bin/env python3
# pip3 install requests

import json
import requests
import re

pages = [
    "https://www.francemusique.fr",
    "https://www.franceculture.fr",
    "https://www.franceinter.fr",
    "https://www.fip.fr",
]

# Regex source: https://regex101.com/r/QzFpaY/1
rgxaac = r"(?P<link>http[^,\"]*?/(?P<title>[^\.]*?)\-hifi\.aac\?id=radiofrance)"
rgxmp3 = r"(?P<link>http[^,\"]*?/(?P<title>[^\.]*?)\.mp3\?id=radiofrance)"

links = {"aac": {}, "mp3": {}}

for p in pages:
    try:
        response = requests.get(p)
        result = re.findall(rgxaac, response.text, 0)
        links["aac"].update({y: x for x, y in result})
        result = re.findall(rgxmp3, response.text, 0)
        links["mp3"].update({y: x for x, y in result})
    except Exception as e:
        print(e)

# JSON View
print()
print("# JSON View")
print(json.dumps(links, indent=1, ensure_ascii=False))

# Markdown View
print()
print("# Markdown View")
for x, y in links["aac"].items():
    print("- [%s](%s)" % (x, y))

# M3U View
print()
print("#EXTM3U")
for x, y in links["aac"].items():
    print("#EXTINF:0,Radio France HiFi - %s\r\n%s" % (x, y))
print()