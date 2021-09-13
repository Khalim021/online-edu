from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView

from shops.forms import CommentModelForm, ShopCommentModelForm
from shops.models import ShopModel, BlogModel, TypeModel


class ShopListView(ListView):
    template_name = 'shop.html'

    def get_queryset(self):
        qs = ShopModel.objects.order_by('-pk')
        qqq = self.request.GET.get('qqq')

        if qqq:
            qs = qs.filter(title__icontains=qqq)

        return qs


class ShopDetailView(DetailView):
    template_name = 'shop_detail.html'
    model = ShopModel


class BlogListView(ListView):
    template_name = 'blog.html'

    def get_queryset(self):
        qs = BlogModel.objects.order_by('-pk')
        qdd = self.request.GET.get('qdd')

        if qdd:
            qs = qs.filter(Q(title__icontains=qdd) |
                           Q(author__icontains=qdd))

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['types'] = TypeModel.objects.all()

        return context


class BlogsDetailView(DetailView):
    template_name = 'blog_detail.html'
    model = BlogModel


class CommentCreateView(CreateView):
    form_class = CommentModelForm

    def form_valid(self, form):
        form.instance.blog = get_object_or_404(BlogModel, pk=self.kwargs.get('pk'))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('shops:blog_detail', kwargs={'pk': self.kwargs.get('pk')})


class ShopCommentCreateView(CreateView):
    form_class = ShopCommentModelForm

    def form_valid(self, form):
        form.instance.shop = get_object_or_404(ShopModel, pk=self.kwargs.get('pk'))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('shops:shop_detail', kwargs={'pk': self.kwargs.get('pk')})
