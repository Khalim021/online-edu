from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CeventsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cevents'
    verbose_name = _('cevents')
