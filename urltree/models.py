# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.db import models

from mptt.models import MPTTModel, TreeForeignKey


class URLTree(models.Model):
    """
    In this Model are the last parsed URLs saved for reusing.
    
    """
    domain = models.CharField(max_length=255, unique=True,
        help_text=_('example: staging.blofeld.ch'))
    created_at = models.DateTimeField(auto_now_add=True, blank=True,
        verbose_name=_(u'Erstellt am'))
    
    def save(self, *args, **kwargs):
        self.domain = self.domain.lstrip('http://')
        self.domain = self.domain.strip('/')
        super(URLTree, self).save(*args, **kwargs)
    
    class Meta:
        ordering = ('-created_at',)
        get_latest_by = ('created_at',)
    
    def __unicode__(self):
        return "URLTree (%s)" % self.domain


class URLNode(MPTTModel):
    urltree = models.ForeignKey(URLTree, related_name='nodes')
    url = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=500, blank=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
    
    checked = models.BooleanField(default=False) # was called at least once
    info = models.CharField(max_length=512, blank=True)

    def __unicode__(self):
        return self.url

    class MPTTMeta:
        order_insertion_by = ['url']
        unique_together = ('url', 'urltree',)
