from django import forms

from shops.models import CommentModel, ShopCommentModel


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        exclude = ['created_at', 'blog']


class ShopCommentModelForm(forms.ModelForm):
    class Meta:
        model = ShopCommentModel
        exclude = ['created_at', 'shop']



