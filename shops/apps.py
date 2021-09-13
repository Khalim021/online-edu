from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ShopsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shops'
    verbose_name = _('shops')
