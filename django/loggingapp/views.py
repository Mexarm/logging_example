import logging

import requests
from django.shortcuts import HttpResponse
from .models import MyModel

# Get an instance of a logger
logger = logging.getLogger(__name__)


def logging(request):
    url = 'https://www.google.com/recaptcha/api/siteverify'
    try:
        m = MyModel()
        m.log()
        res = requests.post(url, timeout=10)
        logger.info(f'reponse code {res.status_code}')
        logger.error('example error')
        logger.warning('example waning')
        logger.critical('example critical')
    except requests.exceptions.ConnectionError:
        logger.exception(f'cannot connect to recaptcha API {url}')

    # print(dir(request))
    return HttpResponse('hola mundo')
