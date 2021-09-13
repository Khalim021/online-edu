from django.urls import path

from home.views import HomeTemplateView, ContactCreateView, AboutDetailView

app_name = 'home'

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('contact/', ContactCreateView.as_view(), name='contact'),
]






