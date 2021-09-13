from django.urls import reverse
from django.views.generic import CreateView, ListView, DetailView

from courses.models import CourseModel, SpeakerModel
from home.forms import ContactModelForm
from home.models import PagesModel
from shops.models import ShopModel, BlogModel


class HomeTemplateView(ListView):
    template_name = 'index.html'

    def get_queryset(self):
        qs = PagesModel.objects.order_by('-pk')
        q = self.request.GET.get('q')

        if q:
            qs = qs.filter(title__icontains=q)

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = CourseModel.objects.all()
        context['speakers'] = SpeakerModel.objects.all()[:4]
        context['shops'] = ShopModel.objects.all()[:4]

        return context


class AboutDetailView(DetailView):
    template_name = 'about.html'


class ContactCreateView(CreateView):
    template_name = 'contact.html'
    form_class = ContactModelForm

    def get_success_url(self):
        return reverse('home:contact')
