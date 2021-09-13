from django.db import models
from django.utils.translation import ugettext_lazy as _


class PagesModel(models.Model):
    title = models.CharField(max_length=75, verbose_name=_('title'))
    banner = models.ImageField(upload_to='banner', verbose_name=_('banner'))
    short_description = models.TextField(verbose_name=_('short_description'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('page')
        verbose_name_plural = _('pages')


class ContactModel(models.Model):
    name = models.CharField(max_length=25, verbose_name=_('name'))
    phone = models.IntegerField(verbose_name=_('phone'))
    email = models.EmailField(verbose_name=_('email'))
    subject = models.CharField(max_length=35, verbose_name=_('subject'))
    message = models.TextField(verbose_name=_('message'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('contact')
        verbose_name_plural = _('contacts')


