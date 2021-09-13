from ckeditor.fields import RichTextField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _

from courses.models import SpeakerModel


class TypeModel(models.Model):
    title = models.CharField(max_length=17, verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('type')
        verbose_name_plural = _('types')


class BlogModel(models.Model):
    title = models.CharField(max_length=150, verbose_name=_('title'))
    banner = models.ImageField(upload_to='banner', verbose_name=_('banner'))
    author = models.CharField(max_length=35, verbose_name=_('author'))
    types = models.ForeignKey(TypeModel, default=False,
                              on_delete=models.CASCADE,
                              related_name='blog',
                              verbose_name=_('types'))
    short_description = models.TextField(verbose_name=_('short_description'))
    long_description = RichTextField(verbose_name=_('long_description'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('blog')
        verbose_name_plural = _('blogs')


class CommentModel(models.Model):
    blog = models.ForeignKey(BlogModel, default=False,
                             on_delete=models.CASCADE,
                             related_name='comments',
                             verbose_name=_('blog'))
    first_name = models.CharField(max_length=25, default=False, verbose_name=_('first_name'))
    last_name = models.CharField(max_length=25, default=False, verbose_name=_('last_name'))
    comment = models.TextField(verbose_name=_('comment'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created-at'))

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = _('blog comment')
        verbose_name_plural = _('blog comments')


class ShopModel(models.Model):
    title = models.CharField(max_length=25, verbose_name=_('title'))
    image = models.ImageField(upload_to='shop', verbose_name=_('image'))
    price = models.FloatField(verbose_name=_('price'))
    real_price = models.FloatField(verbose_name=_('real_price'), default=0)
    discount = models.PositiveIntegerField(default=0,
                                           validators=[
                                               MinValueValidator(0),
                                               MaxValueValidator(100)
                                           ], verbose_name=_('discount'))

    banner = models.ImageField(upload_to='banner', verbose_name=_('banner'))
    short_description = models.TextField(verbose_name=_('short_description'))
    long_description = RichTextField(verbose_name=_('long_description'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    def is_discount(self):
        return self.discount != 0

    def get_price(self):
        if self.is_discount():
            return self.price - self.price * self.discount / 100
        return self.price

    class Meta:
        verbose_name = _('shop')
        verbose_name_plural = _('shops')


class ShopImageModel(models.Model):
    shop = models.ForeignKey(ShopModel,
                             related_name='images',
                             on_delete=models.CASCADE,
                             verbose_name=_('product')
                             )
    image = models.ImageField(upload_to='shop', verbose_name=_('image'))

    def __str__(self):
        return self.shop.title

    class Meta:
        verbose_name = _('shop image')
        verbose_name_plural = _('shop images')


class ShopCommentModel(models.Model):
    shop = models.ForeignKey(ShopModel, default=False,
                             on_delete=models.CASCADE,
                             related_name='comments',
                             verbose_name=_('shop'))
    first_name = models.CharField(max_length=40, verbose_name=_('first_name'))
    last_name = models.CharField(max_length=25, verbose_name=_('last_name'))
    comment = models.TextField(verbose_name=_('comment'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created-at'))

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = _('shop comment')
        verbose_name_plural = _('shop comments')
