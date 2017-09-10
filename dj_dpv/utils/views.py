from lxml import html
import requests

from django.shortcuts import render
from django.conf import settings

import twitter

from locale import atof, setlocale, LC_NUMERIC


def get_api():
    api = twitter.Api(consumer_key=settings.TWITTER_CONSUMER_KEY,
                      consumer_secret=settings.TWITTER_CONSUMER_SECRET,
                      access_token_key=settings.TWITTER_ACCESS_TOKEN,
                      access_token_secret=settings.TWITTER_ACCESS_TOKEN_SECRET)
    return api


def get_description_user(screen_name):
    api = get_api()
    return api.GetUser(screen_name=screen_name).description


def get_bs(description):
    setlocale(LC_NUMERIC, '')
    bs = description.split("Bs. ")[1].split()[0]
    return atof(bs)


def get_peso_info():
    web = settings.PESO_INFO_FROM
    page = requests.get(web)
    tree = html.fromstring(page.content)
    peso = tree.xpath('//span[@class="cm_vds"]/text()')[0]
    peso = peso.split('$ ')[1].split(' ')[0]
    return peso


def get_peso():
    setlocale(LC_NUMERIC, '')
    peso = get_peso_info()
    return atof(peso)
