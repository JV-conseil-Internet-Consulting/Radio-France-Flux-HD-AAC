#!/usr/bin/env python3
# coding: utf-8
# pip3 install requests

import json
import requests
import re


class ScrapRadioFrance():
    """
    Les nouveaux flux web audio Hifi HD
    au format .aac des stations de Radio France
    """

    def __init__(self, pages=[], regex={}, filename="radio-france-aac"):
        self.pages = pages if pages else [
            "https://www.franceculture.fr",
            "https://www.franceinter.fr",
            "https://www.francemusique.fr",
            "https://www.fip.fr"
        ]
        self.regex = regex if regex else {  # Regex source: https://regex101.com/r/QzFpaY/1
            "aac": r"(?P<link>http[^,\"]*?/(?P<title>[^\.]*?)\-hifi\.aac\?id=radiofrance)",
            "mp3": r"(?P<link>http[^,\"]*?/(?P<title>[^\.]*?)\.mp3\?id=radiofrance)"
        }
        self.links = {k: {} for k, v in self.regex.items()}
        self.filename = filename

    def run(self):
        for p in self.pages:
            try:
                response = requests.get(p)
                for k, rgx in self.regex.items():
                    result = re.findall(rgx, response.text, 0)
                    self.links[k].update({y: x for x, y in result})
            except Exception as e:
                print(e)

        # JSON View
        with open("output/%s.json" % self.filename, "w", encoding="UTF-8") as f:
            json.dump(self.links, f, ensure_ascii=False)
            f.close()

        print("\r\n# JSON View\r\n\r\n%s" % json.dumps(self.links, indent=2, ensure_ascii=False))

        # Markdown View
        md = "# Markdown View"
        for type, uri in self.links.items():
            md += "\r\n\r\n## %s:\r\n" % (type)
            for x, y in uri.items():
                md += "\r\n- [%s](%s)" % (x, y)
        with open("output/%s.md" % self.filename, "w", encoding="UTF-8") as f:
            f.write(md)
            f.close()

        print("\r\n%s\r\n" % md)

        # M3U View
        m3u8 = "#EXTM3U\r\n"
        for x, y in self.links["aac"].items():
            m3u8 += ("#EXTINF:0,Radio France HiFi - %s\r\n%s\r\n" % (x, y))

        with open("output/%s.m3u8" % self.filename, "w", encoding="UTF-8") as f:
            f.write(m3u8)
            f.close()

        print("\r\n%s\r\n" % m3u8)
