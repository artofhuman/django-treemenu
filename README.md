#django-treemenu

Another reusable app for organize tree menus on django site

##Install

    pip install git+git+git://github.com/artofhuman/django-treemenu

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


