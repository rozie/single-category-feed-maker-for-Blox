#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import argparse
from bs4 import BeautifulSoup


def main():
    args = parse_arguments()
    url = args.url
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml-xml')

    # head
    print('<?xml version="1.0" encoding="utf-8"?>')
    print('<rss version="2.0">')
    print('<channel>')
    print soup.channel.title
    print soup.channel.link
    print soup.channel.description
    print soup.channel.lastBuildDate

    # body
    for item in soup.findAll("item"):
        if item.category.text == args.category:
            print(item)

    # end
    print('</channel>')
    print('</rss>')


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Script grabs sitemap, returns URLs')

    parser.add_argument(
        '--url', required=False,
        default='http://rozie.blox.pl/rss2',
        help='RSS URL to fetch')
    parser.add_argument(
        '--category', required=False,
        default='DSP2017',
        help='category to extract')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    main()
