from django.conf import settings
from jinja2 import Environment, FileSystemLoader

def environment(**options):
    env = Environment(**options)
    env.loader = FileSystemLoader(settings.JINJA2_TEMPLATE_DIRS)
    return env
