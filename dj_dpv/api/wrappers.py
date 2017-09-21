# -*- coding: utf-8 -*-
import requests
from django.conf import settings


# Definition Functions basic
def base_request(url_path):
    """
        Do a GET to the REST API and return a JSON with the requests response
    """
    response = requests.get(settings.URL_API + url_path)
    if response.status_code != 200:
        return response
    else:
        return response.json()


def base_post(url_path, content):
    """
        Do a POST to the REST API
    """
    response = requests.post(url=settings.URL_API + url_path, json=content)
    return response


def base_put(url_path, content):
    """
        Do a PUT to the REST API
    """
    response = requests.put(url=settings.URL_API + url_path, json=content)
    return response


def base_delete(url_path):
    """
        Do a DELETE to the REST API
    """
    response = requests.delete(url=settings.URL_API + url_path)
    return response

# End functions basics
