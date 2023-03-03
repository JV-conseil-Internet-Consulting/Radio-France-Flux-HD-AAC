# Les nouveaux flux web audio Hifi HD au format .aac des stations de Radio France :radio:

[![made-with-bash](https://img.shields.io/badge/-Made%20with%20Bash-1f425f.svg?logo=image%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyZpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw%2FeHBhY2tldCBiZWdpbj0i77u%2FIiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8%2BIDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuNi1jMTExIDc5LjE1ODMyNSwgMjAxNS8wOS8xMC0wMToxMDoyMCAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENDIDIwMTUgKFdpbmRvd3MpIiB4bXBNTTpJbnN0YW5jZUlEPSJ4bXAuaWlkOkE3MDg2QTAyQUZCMzExRTVBMkQxRDMzMkJDMUQ4RDk3IiB4bXBNTTpEb2N1bWVudElEPSJ4bXAuZGlkOkE3MDg2QTAzQUZCMzExRTVBMkQxRDMzMkJDMUQ4RDk3Ij4gPHhtcE1NOkRlcml2ZWRGcm9tIHN0UmVmOmluc3RhbmNlSUQ9InhtcC5paWQ6QTcwODZBMDBBRkIzMTFFNUEyRDFEMzMyQkMxRDhEOTciIHN0UmVmOmRvY3VtZW50SUQ9InhtcC5kaWQ6QTcwODZBMDFBRkIzMTFFNUEyRDFEMzMyQkMxRDhEOTciLz4gPC9yZGY6RGVzY3JpcHRpb24%2BIDwvcmRmOlJERj4gPC94OnhtcG1ldGE%2BIDw%2FeHBhY2tldCBlbmQ9InIiPz6lm45hAAADkklEQVR42qyVa0yTVxzGn7d9Wy03MS2ii8s%2BeokYNQSVhCzOjXZOFNF4jx%2BMRmPUMEUEqVG36jo2thizLSQSMd4N8ZoQ8RKjJtooaCpK6ZoCtRXKpRempbTv5ey83bhkAUphz8fznvP8znn%2B%2F3NeEEJgNBoRRSmz0ub%2FfuxEacBg%2FDmYtiCjgo5NG2mBXq%2BH5I1ogMRk9Zbd%2BQU2e1ML6VPLOyf5tvBQ8yT1lG10imxsABm7SLs898GTpyYynEzP60hO3trHDKvMigUwdeaceacqzp7nOI4n0SSIIjl36ao4Z356OV07fSQAk6xJ3XGg%2BLCr1d1OYlVHp4eUHPnerU79ZA%2F1kuv1JQMAg%2BE4O2P23EumF3VkvHprsZKMzKwbRUXFEyTvSIEmTVbrysp%2BWr8wfQHGK6WChVa3bKUmdWou%2BjpArdGkzZ41c1zG%2Fu5uGH4swzd561F%2BuhIT4%2BLnSuPsv9%2BJKIpjNr9dXYOyk7%2FBZrcjIT4eCnoKgedJP4BEqhG77E3NKP31FO7cfQA5K0dSYuLgz2TwCWJSOBzG6crzKK%2BohNfni%2Bx6OMUMMNe%2Fgf7ocbw0v0acKg6J8Ql0q%2BT%2FAXR5PNi5dz9c71upuQqCKFAD%2BYhrZLEAmpodaHO3Qy6TI3NhBpbrshGtOWKOSMYwYGQM8nJzoFJNxP2HjyIQho4PewK6hBktoDcUwtIln4PjOWzflQ%2Be5yl0yCCYgYikTclGlxadio%2BBQCSiW1UXoVGrKYwH4RgMrjU1HAB4vR6LzWYfFUCKxfS8Ftk5qxHoCUQAUkRJaSEokkV6Y%2F%2BJUOC4hn6A39NVXVBYeNP8piH6HeA4fPbpdBQV5KOx0QaL1YppX3Jgk0TwH2Vg6S3u%2BdB91%2B%2FpuNYPYFl5uP5V7ZqvsrX7jxqMXR6ff3gCQSTzFI0a1TX3wIs8ul%2Bq4HuWAAiM39vhOuR1O1fQ2gT%2F26Z8Z5vrl2OHi9OXZn995nLV9aFfS6UC9JeJPfuK0NBohWpCHMSAAsFe74WWP%2BvT25wtP9Bpob6uGqqyDnOtaeumjRu%2ByFu36VntK%2FPA5umTJeUtPWZSU9BCgud661odVp3DZtkc7AnYR33RRC708PrVi1larW7XwZIjLnd7R6SgSqWSNjU1B3F72pz5TZbXmX5vV81Yb7Lg7XT%2FUXriu8XLVqw6c6XqWnBKiiYU%2BMt3wWF7u7i91XlSEITwSAZ%2FCzAAHsJVbwXYFFEAAAAASUVORK5CYII%3D)](https://www.gnu.org/software/bash/)
[![License BSD 3-Clause](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](LICENSE)
[![Follow JV conseil on StackOverflow](https://img.shields.io/stackexchange/stackoverflow/r/2477854)](https://stackoverflow.com/users/2477854/jv-conseil "Follow JV conseil on StackOverflow")
[![Become a sponsor to JV-conseil](https://img.shields.io/static/v1?label=Sponsor&message=%E2%9D%A4&logo=GitHub&color=%23fe8e86)](https://github.com/sponsors/JV-conseil "Become a sponsor to JV-conseil")
[![Follow JVconseil on Twitter](https://img.shields.io/twitter/follow/JVconseil.svg?style=social&logo=twitter)](https://twitter.com/JVconseil "Follow JVconseil on Twitter")
[![Follow JVconseil on Mastodon](https://img.shields.io/mastodon/follow/109896584320509054?domain=https%3A%2F%2Ffosstodon.org)](https://fosstodon.org/@JVconseil "Follow JVconseil@fosstodon.org on Mastodon")
[![Follow JV conseil on GitHub](https://img.shields.io/github/followers/JV-conseil?label=JV-conseil&style=social)](https://github.com/JV-conseil "Follow JV-conseil on GitHub")



![Les Stations de Radio France](https://cdn.radiofrance.fr/s3/cruiser-production/2016/12/0b21680a-3c67-4f2d-9e20-be16e67c3e91/600x337_7radios-1.jpg "Les Stations de Radio France")

![Radio-France-Flux-HD-AAC-2](https://user-images.githubusercontent.com/8126807/67148713-d72a2d00-f2a2-11e9-8050-83de5ed8c15f.png)
![Radio-France-Flux-HD-AAC-1](https://user-images.githubusercontent.com/8126807/67148712-d72a2d00-f2a2-11e9-8e51-0155fc8b9b18.png)

```bash
Canaux : Stéréo
Fréquence d'échantillonnage : 48000 Hz
Bits par échantillon : 32
```

## France Musique :

- [francemusiqueeasyclassique](https://icecast.radiofrance.fr/francemusiqueeasyclassique-hifi.aac?id=radiofrance)
- [francemusiqueopera](https://icecast.radiofrance.fr/francemusiqueopera-hifi.aac?id=radiofrance)
- [francemusiquebaroque](https://icecast.radiofrance.fr/francemusiquebaroque-hifi.aac?id=radiofrance)
- [francemusiqueclassiqueplus](https://icecast.radiofrance.fr/francemusiqueclassiqueplus-hifi.aac?id=radiofrance)
- [francemusiqueconcertsradiofrance](https://icecast.radiofrance.fr/francemusiqueconcertsradiofrance-hifi.aac?id=radiofrance)
- [francemusiquelajazz](https://icecast.radiofrance.fr/francemusiquelajazz-hifi.aac?id=radiofrance)
- [francemusiquelacontemporaine](https://icecast.radiofrance.fr/francemusiquelacontemporaine-hifi.aac?id=radiofrance)
- [francemusiqueocoramonde](https://icecast.radiofrance.fr/francemusiqueocoramonde-hifi.aac?id=radiofrance)
- [francemusiquelabo](https://icecast.radiofrance.fr/francemusiquelabo-hifi.aac?id=radiofrance)
- [francemusique](https://icecast.radiofrance.fr/francemusique-hifi.aac?id=radiofrance)

## FiP :

- [fiprock](https://icecast.radiofrance.fr/fiprock-hifi.aac?id=radiofrance)
- [fipjazz](https://icecast.radiofrance.fr/fipjazz-hifi.aac?id=radiofrance)
- [fipgroove](https://icecast.radiofrance.fr/fipgroove-hifi.aac?id=radiofrance)
- [fippop](https://icecast.radiofrance.fr/fippop-hifi.aac?id=radiofrance)
- [fipelectro](https://icecast.radiofrance.fr/fipelectro-hifi.aac?id=radiofrance)
- [fipworld](https://icecast.radiofrance.fr/fipworld-hifi.aac?id=radiofrance)
- [fipreggae](https://icecast.radiofrance.fr/fipreggae-hifi.aac?id=radiofrance)
- [fipnouveautes](https://icecast.radiofrance.fr/fipnouveautes-hifi.aac?id=radiofrance)
- [fip](https://icecast.radiofrance.fr/fip-hifi.aac?id=radiofrance)

## France Culture, France Inter...

- [franceculture](https://icecast.radiofrance.fr/franceculture-hifi.aac?id=radiofrance)
- [franceinter](https://icecast.radiofrance.fr/franceinter-hifi.aac?id=radiofrance)

# iTunes Playlist Import/Export in XML format

`Fichier > Bibliothèque > Exporter la playlist... > Format XML`

![itunes-export-playlist](https://user-images.githubusercontent.com/8126807/67147939-06886c00-f29a-11e9-85a9-1b902c30ef73.jpg)

#### Télécharger le fichier et retirer le suffixe `.txt` du nom du fichier avant importation:

- [Radio France AAC.xml.TXT](https://github.com/JV-conseil-Internet-Consulting/Radio-France-Flux-HD-AAC/files/3746923/Radio.France.AAC.xml.TXT)
- [Radio France AAC.m3u8.TXT](https://github.com/JV-conseil-Internet-Consulting/Radio-France-Flux-HD-AAC/files/3746929/Radio.France.AAC.m3u8.TXT)

# Python Web Scraping

```py
#!/usr/bin/env bash
# -*- coding: UTF-8 -*-
#
# author        : JV-conseil
# credits       : JV-conseil
# licence       : BSD 3-Clause License
# copyright     : Copyright (c) 2019-2023 JV-conseil
#                 All rights reserved
#====================================================

import json
import re

try:
    import requests
except:
    pip install requests

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

# M3U View
print("\r\n#EXTM3U")
for x, y in links["aac"].items():
    print("#EXTINF:0,Radio France HiFi - %s\r\n%s" % (x, y))
print()
```

*[France Musique .AAC link scraping on Regex101](https://regex101.com/r/QzFpaY/1)*

```json
{
  "aac": {
    "francemusiqueeasyclassique": "https://icecast.radiofrance.fr/francemusiqueeasyclassique-hifi.aac?id=radiofrance",
    "francemusiqueopera": "https://icecast.radiofrance.fr/francemusiqueopera-hifi.aac?id=radiofrance",
    "francemusiquebaroque": "https://icecast.radiofrance.fr/francemusiquebaroque-hifi.aac?id=radiofrance",
    "francemusiqueclassiqueplus": "https://icecast.radiofrance.fr/francemusiqueclassiqueplus-hifi.aac?id=radiofrance",
    "francemusiqueconcertsradiofrance": "https://icecast.radiofrance.fr/francemusiqueconcertsradiofrance-hifi.aac?id=radiofrance",
    "francemusiquelajazz": "https://icecast.radiofrance.fr/francemusiquelajazz-hifi.aac?id=radiofrance",
    "francemusiquelacontemporaine": "https://icecast.radiofrance.fr/francemusiquelacontemporaine-hifi.aac?id=radiofrance",
    "francemusiqueocoramonde": "https://icecast.radiofrance.fr/francemusiqueocoramonde-hifi.aac?id=radiofrance",
    "francemusiquelabo": "https://icecast.radiofrance.fr/francemusiquelabo-hifi.aac?id=radiofrance",
    "francemusique": "https://icecast.radiofrance.fr/francemusique-hifi.aac?id=radiofrance",
    "franceculture": "https://icecast.radiofrance.fr/franceculture-hifi.aac?id=radiofrance",
    "franceinter": "https://icecast.radiofrance.fr/franceinter-hifi.aac?id=radiofrance",
    "fiprock": "https://icecast.radiofrance.fr/fiprock-hifi.aac?id=radiofrance",
    "fipjazz": "https://icecast.radiofrance.fr/fipjazz-hifi.aac?id=radiofrance",
    "fipgroove": "https://icecast.radiofrance.fr/fipgroove-hifi.aac?id=radiofrance",
    "fippop": "https://icecast.radiofrance.fr/fippop-hifi.aac?id=radiofrance",
    "fipelectro": "https://icecast.radiofrance.fr/fipelectro-hifi.aac?id=radiofrance",
    "fipworld": "https://icecast.radiofrance.fr/fipworld-hifi.aac?id=radiofrance",
    "fipreggae": "https://icecast.radiofrance.fr/fipreggae-hifi.aac?id=radiofrance",
    "fipnouveautes": "https://icecast.radiofrance.fr/fipnouveautes-hifi.aac?id=radiofrance",
    "fip": "https://icecast.radiofrance.fr/fip-hifi.aac?id=radiofrance"
  },
  "mp3": {
    "francemusiqueeasyclassique-midfi": "https://icecast.radiofrance.fr/francemusiqueeasyclassique-midfi.mp3?id=radiofrance",
    "francemusiqueopera-midfi": "https://icecast.radiofrance.fr/francemusiqueopera-midfi.mp3?id=radiofrance",
    "francemusiquebaroque-midfi": "https://icecast.radiofrance.fr/francemusiquebaroque-midfi.mp3?id=radiofrance",
    "francemusiqueclassiqueplus-midfi": "https://icecast.radiofrance.fr/francemusiqueclassiqueplus-midfi.mp3?id=radiofrance",
    "francemusiqueconcertsradiofrance-midfi": "https://icecast.radiofrance.fr/francemusiqueconcertsradiofrance-midfi.mp3?id=radiofrance",
    "francemusiquelajazz-midfi": "https://icecast.radiofrance.fr/francemusiquelajazz-midfi.mp3?id=radiofrance",
    "francemusiquelacontemporaine-midfi": "https://icecast.radiofrance.fr/francemusiquelacontemporaine-midfi.mp3?id=radiofrance",
    "francemusiqueocoramonde-midfi": "https://icecast.radiofrance.fr/francemusiqueocoramonde-midfi.mp3?id=radiofrance",
    "francemusiquelabo-midfi": "https://icecast.radiofrance.fr/francemusiquelabo-midfi.mp3?id=radiofrance",
    "francemusique-lofi": "https://icecast.radiofrance.fr/francemusique-lofi.mp3?id=radiofrance",
    "francemusique-midfi": "https://icecast.radiofrance.fr/francemusique-midfi.mp3?id=radiofrance",
    "franceculture-midfi": "https://icecast.radiofrance.fr/franceculture-midfi.mp3?id=radiofrance",
    "franceinter-midfi": "https://icecast.radiofrance.fr/franceinter-midfi.mp3?id=radiofrance",
    "franceinter-lofi": "https://icecast.radiofrance.fr/franceinter-lofi.mp3?id=radiofrance",
    "fiprock-midfi": "https://icecast.radiofrance.fr/fiprock-midfi.mp3?id=radiofrance",
    "fipjazz-midfi": "https://icecast.radiofrance.fr/fipjazz-midfi.mp3?id=radiofrance",
    "fipgroove-midfi": "https://icecast.radiofrance.fr/fipgroove-midfi.mp3?id=radiofrance",
    "fippop-midfi": "https://icecast.radiofrance.fr/fippop-midfi.mp3?id=radiofrance",
    "fipelectro-midfi": "https://icecast.radiofrance.fr/fipelectro-midfi.mp3?id=radiofrance",
    "fipworld-midfi": "https://icecast.radiofrance.fr/fipworld-midfi.mp3?id=radiofrance",
    "fipreggae-midfi": "https://icecast.radiofrance.fr/fipreggae-midfi.mp3?id=radiofrance",
    "fipnouveautes-midfi": "https://icecast.radiofrance.fr/fipnouveautes-midfi.mp3?id=radiofrance",
    "fip-lofi": "https://icecast.radiofrance.fr/fip-lofi.mp3?id=radiofrance",
    "fip-midfi": "https://icecast.radiofrance.fr/fip-midfi.mp3?id=radiofrance",
    "fipbordeaux-lofi": "https://icecast.radiofrance.fr/fipbordeaux-lofi.mp3?id=radiofrance",
    "fipbordeaux-midfi": "https://icecast.radiofrance.fr/fipbordeaux-midfi.mp3?id=radiofrance",
    "fipnantes-lofi": "https://icecast.radiofrance.fr/fipnantes-lofi.mp3?id=radiofrance",
    "fipnantes-midfi": "https://icecast.radiofrance.fr/fipnantes-midfi.mp3?id=radiofrance",
    "fipstrasbourg-lofi": "https://icecast.radiofrance.fr/fipstrasbourg-lofi.mp3?id=radiofrance",
    "fipstrasbourg-midfi": "https://icecast.radiofrance.fr/fipstrasbourg-midfi.mp3?id=radiofrance"
  }
}
```

## Open API de Radio France

> L’Open API de Radio France est un portail qui permet à des acteurs innovants de développer de nouveaux services grâce à un accès raisonné aux contenus de Radio France — https://www.radiofrance.fr/lopen-api-radio-france

## Sponsorship

If this project helps you, you can offer me a cup of coffee ☕️ :-)

[![Become a sponsor to JV-conseil](https://img.shields.io/static/v1?label=Sponsor&message=%E2%9D%A4&logo=GitHub&color=%23fe8e86)](https://github.com/sponsors/JV-conseil)
