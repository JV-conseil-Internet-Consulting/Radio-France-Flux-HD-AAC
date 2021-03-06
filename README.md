[![Donate with PayPal](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=P3DGL6EANDY96&source=url)
[![License BSD 3-Clause](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](LICENSE)
[![Follow JV conseil – Internet Consulting on Twitter](https://img.shields.io/twitter/follow/JVconseil.svg?style=social&logo=twitter)](https://twitter.com/JVconseil)

# Les nouveaux flux web audio Hifi HD au format .aac des stations de Radio France

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

# Open API de Radio France

> L’Open API de Radio France est un portail qui permet à des acteurs innovants de développer de nouveaux services grâce à un accès raisonné aux contenus de Radio France — https://www.radiofrance.fr/lopen-api-radio-france
