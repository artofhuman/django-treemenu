#coding: utf-8
from __future__ import unicode_literals

from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.dispatch import receiver
from django.core.cache import cache
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Menu(models.Model):
    title = models.CharField(verbose_name='Название меню', max_length=50)
    slug = models.SlugField()

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class MenuItem(MPTTModel):
    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'
        ordering = ['tree_id', 'lft']

    active = models.BooleanField(verbose_name='Активность', default=True)
    menu = models.ForeignKey(Menu, verbose_name='Меню', related_name='menu_items')
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', verbose_name='Родительский пункт')
    title = models.CharField(verbose_name='Название  меню', max_length=50)
    url = models.CharField(max_length=100, help_text='Ссылка, например /about/ или http://foo.com/')

    def __str__(self):
        return self.title

    def title_with_spacer(self):
        '''
        make title with spaces for show in admin
        '''
        spacer = ''
        for i in range(0, self.level):
            spacer += u'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'
        return spacer + self.title


@receiver(models.signals.post_save, sender=MenuItem)
@receiver(models.signals.pre_delete, sender=MenuItem)
def invalidate(instance, **kwargs):
    cache.delete('treemenu/%s' % (instance.menu.slug))
