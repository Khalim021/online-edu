from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CoursesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'courses'
    verbose_name = _('courses')
