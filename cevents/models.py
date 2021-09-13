from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import ugettext_lazy as _


class EventsModel(models.Model):
    title = models.CharField(max_length=150, verbose_name=_('title'))
    image = models.ImageField(upload_to='cevents', verbose_name=_('image'))
    event_location = models.CharField(max_length=25, default=False, verbose_name=_('event_location'))
    short_description = models.TextField(default=False, verbose_name=_('short_description'))
    long_description = RichTextField(verbose_name=_('long_description'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('event')
        verbose_name_plural = _('events')
