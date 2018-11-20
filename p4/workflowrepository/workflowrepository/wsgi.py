"""
WSGI config for workflowrepository project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os,sys

from django.core.wsgi import get_wsgi_application
from dj_static import Cling

sys.path.append("/home/sliezzan/.virtualenvs/pyc_psi_2-1/lib/python2.7/site-packages")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "workflowrepository.settings")

application =  Cling(get_wsgi_application())
