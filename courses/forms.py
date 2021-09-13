from django import forms

from courses.models import CourseCommentModel, SpeakerCommentModel


class SpeakerCommentModelForm(forms.ModelForm):
    class Meta:
        model = SpeakerCommentModel
        exclude = ['created_at', 'speaker']


class CourseCommentModelForm(forms.ModelForm):
    class Meta:
        model = CourseCommentModel
        exclude = ['created_at', 'courses']














