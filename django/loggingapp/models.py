from django.db import models

import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

class MyModel(models.Model):
    def log(self):
        logger.info('example info')
        logger.error('example error')
        logger.warning('example waning')
        logger.critical('example critical')
