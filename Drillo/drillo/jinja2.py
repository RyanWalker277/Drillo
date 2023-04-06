# from django.conf import settings
# from jinja2 import Environment, FileSystemLoader

# def environment(**options):
#     env = Environment(**options)
#     env.loader = FileSystemLoader(settings.JINJA2_TEMPLATE_DIRS)
#     return env
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from django.urls.exceptions import NoReverseMatch
from django.conf import settings
from jinja2 import Environment, FileSystemLoader

def environment(**options):
    env = Environment(**options)
    env.loader = FileSystemLoader(settings.JINJA2_TEMPLATE_DIRS)

    try:
        # Set the value for the 'static' function in the Jinja2 environment globals
        env.globals['static'] = staticfiles_storage.url
    except NoReverseMatch:
        pass

    env.globals['url'] = reverse

    return env
