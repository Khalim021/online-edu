from django.urls import path

from cevents.views import EventListView, EventDetailView

app_name = 'events'

urlpatterns = [
    path('', EventListView.as_view(), name='event'),
    path('<int:pk>/', EventDetailView.as_view(), name='event_detail'),
]


