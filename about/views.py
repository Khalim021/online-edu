from django.views.generic import TemplateView

from about.models import PartnerModel


class AboutTemplateView(TemplateView):
    template_name = 'about.html'
    queryset = PartnerModel.objects.order_by('-pk')




