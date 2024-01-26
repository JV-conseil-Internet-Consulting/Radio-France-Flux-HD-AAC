# Les nouveaux flux web audio Hifi HD au format .aac des stations de Radio France :radio:

![visitors](https://visitor-badge.laobi.icu/badge?page_id=JV-conseil-Internet-Consulting.Radio-France-Flux-HD-AAC)
[![pages-build-deployment](https://github.com/JV-conseil-Internet-Consulting/Radio-France-Flux-HD-AAC/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/JV-conseil-Internet-Consulting/Radio-France-Flux-HD-AAC/actions/workflows/pages/pages-build-deployment)
[![License EUPL 1.2](https://img.shields.io/badge/License-EUPL--1.2-blue.svg)](https://github.com/JV-conseil/.github/blob/main/LICENSE "License EUPL 1.2")
[![Become a sponsor to JV-conseil](https://img.shields.io/static/v1?label=Sponsor&message=%E2%9D%A4&logo=GitHub&color=%23fe8e86)](https://github.com/sponsors/JV-conseil "Become a sponsor to JV-conseil")
[![Follow JV conseil on StackOverflow](https://img.shields.io/stackexchange/stackoverflow/r/2477854)](https://stackoverflow.com/users/2477854/jv-conseil "Follow JV conseil on StackOverflow")
[![Follow JVconseil on Twitter](https://img.shields.io/twitter/follow/JVconseil.svg?style=social&logo=twitter)](https://twitter.com/JVconseil "Follow JVconseil on Twitter")
[![Follow JVconseil on Mastodon](https://img.shields.io/mastodon/follow/109896584320509054?domain=https%3A%2F%2Ffosstodon.org)](https://fosstodon.org/@JVconseil "Follow JVconseil@fosstodon.org on Mastodon")
[![Follow JV conseil on GitHub](https://img.shields.io/github/followers/JV-conseil?label=JV-conseil&style=social)](https://github.com/JV-conseil "Follow JV-conseil on GitHub")

![Les Stations de Radio France](https://www.jv-conseil.net/assets/posts/2020-10-16-radio-france-flux-hd-aac.jpg "Les Stations de Radio France")

![Radio-France-Flux-HD-AAC-2](https://user-images.githubusercontent.com/8126807/67148713-d72a2d00-f2a2-11e9-8050-83de5ed8c15f.png)
![Radio-France-Flux-HD-AAC-1](https://user-images.githubusercontent.com/8126807/67148712-d72a2d00-f2a2-11e9-8e51-0155fc8b9b18.png)

```bash
Canaux : Stéréo
Fréquence d'échantillonnage : 48000 Hz
Bits par échantillon : 32
```

## France Musique

1. [francemusique](https://icecast.radiofrance.fr/francemusique-hifi.aac?id=radiofrance)
2. [francemusiquebaroque](https://icecast.radiofrance.fr/francemusiquebaroque-hifi.aac?id=radiofrance)
3. [francemusiqueclassiqueplus](https://icecast.radiofrance.fr/francemusiqueclassiqueplus-hifi.aac?id=radiofrance)
4. [francemusiqueconcertsradiofrance](https://icecast.radiofrance.fr/francemusiqueconcertsradiofrance-hifi.aac?id=radiofrance)
5. [francemusiqueeasyclassique](https://icecast.radiofrance.fr/francemusiqueeasyclassique-hifi.aac?id=radiofrance)
6. [francemusiquelabo](https://icecast.radiofrance.fr/francemusiquelabo-hifi.aac?id=radiofrance)
7. [francemusiquelacontemporaine](https://icecast.radiofrance.fr/francemusiquelacontemporaine-hifi.aac?id=radiofrance)
8. [francemusiquelajazz](https://icecast.radiofrance.fr/francemusiquelajazz-hifi.aac?id=radiofrance)
9. [francemusiqueocoramonde](https://icecast.radiofrance.fr/francemusiqueocoramonde-hifi.aac?id=radiofrance)
10. [francemusiqueopera](https://icecast.radiofrance.fr/francemusiqueopera-hifi.aac?id=radiofrance)

## FiP

1. [fip](https://icecast.radiofrance.fr/fip-hifi.aac?id=radiofrance)
2. [fipelectro](https://icecast.radiofrance.fr/fipelectro-hifi.aac?id=radiofrance)
3. [fipgroove](https://icecast.radiofrance.fr/fipgroove-hifi.aac?id=radiofrance)
4. [fipjazz](https://icecast.radiofrance.fr/fipjazz-hifi.aac?id=radiofrance)
5. [fipnouveautes](https://icecast.radiofrance.fr/fipnouveautes-hifi.aac?id=radiofrance)
6. [fippop](https://icecast.radiofrance.fr/fippop-hifi.aac?id=radiofrance)
7. [fipreggae](https://icecast.radiofrance.fr/fipreggae-hifi.aac?id=radiofrance)
8. [fiprock](https://icecast.radiofrance.fr/fiprock-hifi.aac?id=radiofrance)
9. [fipworld](https://icecast.radiofrance.fr/fipworld-hifi.aac?id=radiofrance)

## France Culture, France Inter

- [franceculture](https://icecast.radiofrance.fr/franceculture-hifi.aac?id=radiofrance)
- [franceinter](https://icecast.radiofrance.fr/franceinter-hifi.aac?id=radiofrance)

# iTunes Playlist Import/Export in XML format

`Fichier > Bibliothèque > Exporter la playlist... > Format XML`

![itunes-export-playlist](https://user-images.githubusercontent.com/8126807/67147939-06886c00-f29a-11e9-85a9-1b902c30ef73.jpg)

#### Télécharger le fichier et retirer le suffixe `.txt` du nom du fichier avant importation

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
# copyright     : Copyright (c) 2019-2024 JV-conseil
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

## Icecast, ICY

```bash
#!/usr/bin/env bash
# -*- coding: UTF-8 -*-
#
# author        : JV-conseil
# credits       : JV-conseil
# copyright     : Copyright (c) 2019-2024 JV-conseil
#                 All rights reserved
#====================================================

cat <<EOF
| attempt | icy-pub | wait |
| :------ | :-----: | ---: |
EOF
for i in {0..10}; do
  wait=$(("${i}" * 10))
  sleep "${wait}"
  tmp="$(curl -sI "http://icecast.radiofrance.fr/franceinter-hifi.aac?icy-pub=0" | grep -o "icy-pub: [0-1]")"
  printf "| %d      | %s |   %d sec. |\n" "${i}" "${tmp}" "${wait}"
done
```

`icy-pub=0` ne désactivera pas les publicités, le paramètre passé dans l'url n'a aucun effet sur la valeur retournée par les en-têtes du serveur.

Le tableau ci-dessous produit par le script ci-dessus démontre que sur 10 tentatives espacées d'un temps d'attente augmenté d'un facteur de 10 secondes entre chacune, l'activation / désactivation de `icy-pub` apparaît alléatoire 👇

| attempt | icy-pub    |     wait |
| :------ | :--------- | -------: |
| 0       | icy-pub: 1 |   0 sec. |
| 1       | icy-pub: 1 |  10 sec. |
| 2       | icy-pub: 1 |  20 sec. |
| 3       | icy-pub: 1 |  30 sec. |
| 4       | icy-pub: 0 |  40 sec. |
| 5       | icy-pub: 0 |  50 sec. |
| 6       | icy-pub: 0 |  60 sec. |
| 7       | icy-pub: 1 |  70 sec. |
| 8       | icy-pub: 1 |  80 sec. |
| 9       | icy-pub: 0 |  90 sec. |
| 10      | icy-pub: 1 | 100 sec. |

Pour aller plus loin documentation sur le protocole [Icecast](https://cast.readme.io/docs/icecast) 🔗

NB: Essayer de changer `icy-br=320` n'a pas plus d'effets et ne bascule pas l'encodage de 192 à 320 Kbps, standard d'écoute disponible sur la BBC depuis déjà plusieurs années 🔉

## Open API de Radio France

> L’Open API de Radio France est un portail qui permet à des acteurs innovants de développer de nouveaux services grâce à un accès raisonné aux contenus de Radio France — <https://www.radiofrance.fr/lopen-api-radio-france>

Documentation

- [Liste des webradios de la marque FIP](https://developers.radiofrance.fr/doc/tutorial-by-example/list-locals-and-webradios)
- [Les technologies qui composent l'Open API et son environnement](https://developers.radiofrance.fr/doc/technologies#les-technologies-qui-composent-lopen-api-et-son-environnement)

## Sponsorship

If this project helps you, you can offer me a cup of coffee ☕️ :-)

[![Become a sponsor to JV-conseil](https://img.shields.io/static/v1?label=Sponsor&message=%E2%9D%A4&logo=GitHub&color=%23fe8e86)](https://github.com/sponsors/JV-conseil)
