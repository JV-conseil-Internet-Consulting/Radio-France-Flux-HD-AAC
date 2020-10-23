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

### France Musique :

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

### FiP :

- [fiprock](https://icecast.radiofrance.fr/fiprock-hifi.aac?id=radiofrance)
- [fipjazz](https://icecast.radiofrance.fr/fipjazz-hifi.aac?id=radiofrance)
- [fipgroove](https://icecast.radiofrance.fr/fipgroove-hifi.aac?id=radiofrance)
- [fippop](https://icecast.radiofrance.fr/fippop-hifi.aac?id=radiofrance)
- [fipelectro](https://icecast.radiofrance.fr/fipelectro-hifi.aac?id=radiofrance)
- [fipworld](https://icecast.radiofrance.fr/fipworld-hifi.aac?id=radiofrance)
- [fipreggae](https://icecast.radiofrance.fr/fipreggae-hifi.aac?id=radiofrance)
- [fipnouveautes](https://icecast.radiofrance.fr/fipnouveautes-hifi.aac?id=radiofrance)
- [fip](https://icecast.radiofrance.fr/fip-hifi.aac?id=radiofrance)

### France Culture, France Inter...

- [franceculture](https://icecast.radiofrance.fr/franceculture-hifi.aac?id=radiofrance)
- [franceinter](https://icecast.radiofrance.fr/franceinter-hifi.aac?id=radiofrance)

### iTunes Playlist Import/Export in XML format

`Fichier > Bibliothèque > Exporter la playlist... > Format XML`

![itunes-export-playlist](https://user-images.githubusercontent.com/8126807/67147939-06886c00-f29a-11e9-85a9-1b902c30ef73.jpg)

#### Télécharger le fichier et retirer le suffixe `.txt` du nom du fichier avant importation:

- [Radio France AAC.xml.TXT](https://github.com/JV-conseil-Internet-Consulting/Radio-France-Flux-HD-AAC/files/3746923/Radio.France.AAC.xml.TXT)
- [Radio France AAC.m3u8.TXT](https://github.com/JV-conseil-Internet-Consulting/Radio-France-Flux-HD-AAC/files/3746929/Radio.France.AAC.m3u8.TXT)

### Python Web Scraping

```py
# coding=utf8
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
regex = r"(?P<link>http[^,\"]*?/(?P<title>[^\.]*?)\-hifi\.aac\?id=radiofrance)"

links = {}

for p in pages:
    try:
        response = requests.get(p)
        result = re.findall(regex, response.text, 0)
        links.update({y: x for x, y in result})
    except Exception as e:
        print(e)

# JSON View
print(json.dumps(links, indent=1, ensure_ascii=False))

# Markdown View
for x, y in links.items():
    print("- [%s](%s)" % (x, y))
```

*[France Musique .AAC link scraping on Regex101](https://regex101.com/r/QzFpaY/1)*

```json
{
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
}
```

### Open API de Radio France

> L’Open API de Radio France est un portail qui permet à des acteurs innovants de développer de nouveaux services grâce à un accès raisonné aux contenus de Radio France. — https://www.radiofrance.fr/lopen-api-radio-france
