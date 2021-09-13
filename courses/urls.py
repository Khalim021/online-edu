from django.urls import path

from courses.views import CourseListView, SpeakerListView, CourseDetailView, SpeakerDetailView, CourseCommentCreateView, \
    CommentCreateView

app_name = 'courses'

urlpatterns = [
    path('', CourseListView.as_view(), name='list'),
    path('<int:pk>/', CourseDetailView.as_view(), name='detail'),
    path('<int:pk>/course-comment/', CourseCommentCreateView.as_view(), name='comment'),
    path('speaker/', SpeakerListView.as_view(), name='speaker'),
    path('<int:pk>/comment/', CommentCreateView.as_view(), name='speaker_comment'),
    path('<int:pk>/speaker/', SpeakerDetailView.as_view(), name='speaker_detail'),

]
