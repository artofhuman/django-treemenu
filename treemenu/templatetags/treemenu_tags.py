from ..models import MenuItem
from django import template
from django.core.cache import cache
from django.conf import settings

register = template.Library()


def build_menu(parser, token):
    """
    {% menu menu_name %}
    """
    try:
        tag_name, menu_name = token.split_contents()
    except:
        raise template.TemplateSyntaxError, "%r tag requires exactly one argument" % token.contents.split()[0]
    return MenuObject(menu_name)


class MenuObject(template.Node):
    def __init__(self, menu_name):
        self.menu_name = menu_name

    def render(self, context):
        current_path = context['request'].path
        context['menuitems'] = get_items(self.menu_name, current_path)
        return ''


def get_items(menu_name, current_path):

    cache_time = getattr(settings, 'TREEMENU_CACHE_TIME', 3600)
    # debug = getattr(settings, 'DEBUG', False)

    menuitems = []
    if cache_time >= 0:
        cache_key = 'treemenu/%s' % (menu_name)
        items = cache.get(cache_key, [])
    else:
        items = []

    if not items:
        items = MenuItem.objects.filter(menu__slug=menu_name, active=True)
        if cache_time >= 0:
            cache.set(cache_key, items, cache_time)

    for i in items:
        current = (i.url != '/' and current_path.startswith(i.url)) or (i.url == '/' and current_path == '/')
        i.current = current
        menuitems.append(i)

    return menuitems

register.tag('menu', build_menu)
