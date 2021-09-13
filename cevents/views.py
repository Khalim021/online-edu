# Create your views here.
from django.views.generic import ListView, DetailView

from cevents.models import EventsModel


class EventListView(ListView):
    template_name = 'events.html'

    def get_queryset(self):
        qs = EventsModel.objects.order_by('-pk')
        ql = self.request.GET.get('ql')

        if ql:
            qs = qs.filter(title__icontains=ql)

        return qs


class EventDetailView(DetailView):
    template_name = 'events_detail.html'
    model = EventsModel
