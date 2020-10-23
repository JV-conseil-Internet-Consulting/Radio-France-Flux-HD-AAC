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
regex = {
    "aac": r"(?P<link>http[^,\"]*?/(?P<title>[^\.]*?)\-hifi\.aac\?id=radiofrance)",
    "mp3": r"(?P<link>http[^,\"]*?/(?P<title>[^\.]*?)\.mp3\?id=radiofrance)"
}

links = {k: {} for k, v in regex.items()}

for p in pages:
    try:
        response = requests.get(p)
        for k, rgx in regex.items():
            result = re.findall(rgx, response.text, 0)
            links[k].update({y: x for x, y in result})
    except Exception as e:
        print(e)

# JSON View
print("\r\n# JSON View\r\n")
print(json.dumps(links, indent=2, ensure_ascii=False))

# Markdown View
print("\r\n# Markdown View\r\n")
for x, y in links["aac"].items():
    print("- [%s](%s)" % (x, y))

for x, y in links["mp3"].items():
    print("- %s: %s" % (x, y))

# M3U View
print("\r\n#EXTM3U")
for x, y in links["aac"].items():
    print("#EXTINF:0,Radio France HiFi - %s\r\n%s" % (x, y))
print()
