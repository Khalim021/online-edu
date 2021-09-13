from django.urls import path

from about.views import AboutTemplateView

app_name = 'about'

urlpatterns = [
    path('', AboutTemplateView.as_view(), name='about')
]


