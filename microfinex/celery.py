from __future__ import absolute_import

import os

from celery import Celery
from microfinex.settings import base

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "microfinex.settings.development")

app = Celery("microfinex")

app.config_from_object("microfinex.settings.development", namespace="CELERY"),

app.autodiscover_tasks(lambda: base.INSTALLED_APPS)