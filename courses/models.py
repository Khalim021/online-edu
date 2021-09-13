from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import ugettext_lazy as _


class CategoryModel(models.Model):
    title = models.CharField(max_length=17, verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')


class SpeakerModel(models.Model):
    name = models.CharField(max_length=25, verbose_name=_('name'))
    image = models.ImageField(upload_to='image', default=False, verbose_name=_('image'))
    bio = models.TextField(verbose_name=_('bio'))
    about = RichTextField(verbose_name=_('about'))
    avatar = models.ImageField(upload_to='avatar', default=False, verbose_name=_('avatar'))
    job = models.CharField(max_length=35, default=False, verbose_name=_('job'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('speaker')
        verbose_name_plural = _('speakers')


class SpeakerCommentModel(models.Model):
    first_name = models.CharField(max_length=35, verbose_name=_('first_name'))
    last_name = models.CharField(max_length=35, verbose_name=_('last_name'))
    speaker = models.ForeignKey(SpeakerModel, default=False,
                                on_delete=models.CASCADE,
                                related_name='comments',
                                verbose_name=_('speaker'))
    comment = models.TextField(verbose_name=_('comment'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created-at'))

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = _('speaker comment')
        verbose_name_plural = _('speaker comments')


class CourseModel(models.Model):
    title = models.CharField(max_length=175, verbose_name=_('title'))
    image = models.ImageField(upload_to='courses', verbose_name=_('image'))
    overview = models.TextField(verbose_name=_('overview'))
    speakers = models.ForeignKey(SpeakerModel,
                                 on_delete=models.CASCADE,
                                 related_name='courses',
                                 verbose_name=_('speaker'))

    categories = models.ForeignKey(CategoryModel,
                                   on_delete=models.CASCADE,
                                   related_name='courses', null=True,
                                   verbose_name=_('categories'))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('course')
        verbose_name_plural = _('courses')


class CourseCommentModel(models.Model):
    first_name = models.CharField(max_length=35, verbose_name=_('first_name'))
    last_name = models.CharField(max_length=30, verbose_name=_('last_name'))
    courses = models.ForeignKey(CourseModel,
                                on_delete=models.CASCADE,
                                related_name='comments',
                                verbose_name=_('courses'),
                                default=False)
    comment = models.TextField(verbose_name=_('comment'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created-at'))

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = _('course comment')
        verbose_name_plural = _('courses comments')
