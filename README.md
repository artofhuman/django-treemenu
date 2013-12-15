#django-treemenu

Another reusable app for organize tree menus on django site
This app need grapelli admin theme

![Alt text](https://raw.github.com/artofhuman/django-treemenu/master/assets/screen.jpg)

##Install from pip

    pip install django-treemenu

##Install from git

    pip install git+git+git://github.com/artofhuman/django-treemenu

Then run python manage syncdb or if your use south run python manage migrate

##Usage

Add treemenu in settings.py
```python
    INSTALLED_APPS = (
        # ...
        treemenu,
        # ...
    )
```
Create menu and in your template

## Examples

Simple menu without childrens

```html
{% load treemenu_tags %}
{% menu you_menu_slug %}
<div class="b-menu-vert b-menu-vert_type_header">
    <ul class="b-menu-vert__layout">
        {% for item in menuitems %}
        <li class="b-menu-vert__layout-unit {% if forloop.first %}b-menu-vert__layout-unit_position_first{% endif %} {% if forloop.last %}b-menu-vert__layout-unit_position_last{% endif %}">
            <div class="b-menu-vert__item">
                <a class="b-link b-menu-vert__root {% if item.current %}b-big{% endif %}" href="{{ item.url }}">{{ item.title }}</a>
            </div>
        </li>
        {% endfor %}
    </ul>
</div>
```

Dropdown menu

```html
{% load treemenu_tags mptt_tags %}
{% menu topmenu %}
<div class="b-menu-horiz b-menu-horiz_layout_normal b-menu-horiz_position_topmenu">
    <ul class="b-menu-horiz__layout">
        <li class="b-menu-horiz__layout-unit b-menu-horiz__layout-unit_position_first"><div class="b-menu-horiz__item b-menu-horiz__item_layout_home {% if request.path == '/'%}b-menu-horiz__item_state_current{% endif %}"><a href="/" class="b-link"><img alt="" src="{{ STATIC_URL }}prazdnik/img/blank.gif" class="b-icon b-icon_type_home"></a></div></li>
        {% recursetree menuitems %}
            <li class="{% if node.level == 0%}b-menu-horiz__layout-unit{% else %}b-menu-vert__layout-unit{% endif %}">
                <div class="
                    {% if node.level == 0%}b-menu-horiz__item{% else %}b-menu-vert__item{% endif %}
                    {% if node.level == 0 and node.current %}b-menu-horiz__item_state_current {% endif %}
                    {% if node.current %}b-menu-vert__item_state_current {% endif %}">
                    <a href="{{ node.url }}" class="b-link">{{ node.title }}</a>
                    {% if not node.is_leaf_node %}
                    <div class="b-menu-horiz__submenu">
                        <div class="b-menu-vert">
                            <ul class="b-menu-vert__layout">
                                {{ children }}
                            </ul>
                        </div>
                    </div>
                    {% endif %}
                </div>
            </li>
        {% endrecursetree %}
    </ul>
</div>
```

[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/artofhuman/django-treemenu/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

