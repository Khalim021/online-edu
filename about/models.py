
from django.db import models
from django.utils.translation import ugettext_lazy as _


class PartnerModel(models.Model):
    logo = models.ImageField(upload_to='logo', verbose_name=_('logo'))
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name=_('updated_at'))

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = _('partner')
        verbose_name_plural = _('partners')
