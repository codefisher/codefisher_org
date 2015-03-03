"""
WSGI config for codefisher project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "codefisher_org.codefisher.settings")
os.environ['PYTHONHASHSEED'] = 'random'
# this is needed for stuff like the git plugin, it will try to write to /home/root/ otherwise
os.environ['HOME'] = os.path.join(os.path.realpath(os.path.dirname(__file__)), '..', '..')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
