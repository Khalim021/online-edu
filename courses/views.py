from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from courses.forms import SpeakerCommentModelForm, CourseCommentModelForm
from courses.models import CourseModel, SpeakerModel


class CourseListView(ListView):
    template_name = 'courses.html'

    def get_queryset(self):
        qs = CourseModel.objects.order_by('-pk')
        qsf = self.request.GET.get('qsf')

        if qsf:
            qs = qs.filter(title__icontains=qsf)

        return qs


class CourseDetailView(DetailView):
    template_name = 'courses_detail.html'
    model = CourseModel


class SpeakerListView(ListView):
    template_name = 'teachers.html'

    def get_queryset(self):
        qsl = SpeakerModel.objects.order_by('-pk')
        qqs = self.request.GET.get('qqs')

        if qqs:
            qsl = qsl.filter(name__icontains=qqs)

        return qsl


class SpeakerDetailView(DetailView):
    template_name = 'about_teachers.html'
    model = SpeakerModel


class CommentCreateView(CreateView):
    form_class = SpeakerCommentModelForm

    def form_valid(self, form):
        form.instance.speaker = get_object_or_404(SpeakerModel, pk=self.kwargs.get('pk'))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('courses:speaker_detail', kwargs={'pk': self.kwargs.get('pk')})


class CourseCommentCreateView(CreateView):
    form_class = CourseCommentModelForm

    def form_valid(self, form):
        form.instance.courses = get_object_or_404(CourseModel, pk=self.kwargs.get('pk'))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('courses:detail', kwargs={'pk': self.kwargs.get('pk')})
