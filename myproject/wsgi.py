"""
WSGI config for myproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from mezzanine.utils.conf import real_project_name

os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "%s.settings" % real_project_name("myproject"))

application = get_wsgi_application()


'''
#Heroku suggestion  https://devcenter.heroku.com/articles/django-app-configuration
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
'''

#FOR HEROKU DEPLOY
'''
from django.core.wsgi import get_wsgi_application
from dj_static import Cling

application = Cling(get_wsgi_application())

'''


from whitenoise import WhiteNoise
application = get_wsgi_application()
application = WhiteNoise(application, root='/myproject/static')
