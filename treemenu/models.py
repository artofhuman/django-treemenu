# -*- coding: utf-8 -*-
#author: Semen Pupkov (semen.pupkov@gmail.com)

from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.dispatch import receiver
from django.core.cache import cache


class Menu(models.Model):

    title = models.CharField(verbose_name=u'Название меню', max_length=50)
    slug = models.SlugField()

    class Meta:
        verbose_name = u'Меню'
        verbose_name_plural = 'Меню'

    def __unicode__(self):
        return self.title


class MenuItem(MPTTModel):
    class Meta:
        verbose_name = u'Пункт меню'
        verbose_name_plural = u'Пункты меню'
        ordering = ['tree_id', 'lft']

    active = models.BooleanField(verbose_name=u'Активность', default=True)
    menu = models.ForeignKey(Menu, verbose_name=u'Меню', related_name='menu_items')
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', verbose_name=u'Родительский пункт')
    title = models.CharField(verbose_name=u'Название  меню', max_length=50)
    url = models.CharField(max_length=100, help_text='Ссылка, например /about/ или http://foo.com/')

    def __unicode__(self):
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
