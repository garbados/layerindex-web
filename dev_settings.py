import os
import hashlib
import random
from settings import *

WORKDIR = os.path.dirname(os.path.realpath(__file__))

SECRET_KEY = hashlib.md5(str(random.random()).format(10).encode('utf-8')).hexdigest()

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('admin', 'admin@example.com'),
)

DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3'
DATABASES['default']['NAME'] = os.sep.join([WORKDIR, 'layerindex-sql'])

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

LAYER_FETCH_DIR = os.sep.join([WORKDIR, "layers"])
