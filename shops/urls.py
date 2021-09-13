from django.urls import path

from shops.views import ShopListView, BlogListView, BlogsDetailView, ShopDetailView, ShopCommentCreateView, \
    CommentCreateView

app_name = 'shops'

urlpatterns = [
    path('shops/', ShopListView.as_view(), name='shops'),
    path('shops/<int:pk>/', ShopDetailView.as_view(), name='shop_detail'),
    path('<int:pk>/shop-comment', ShopCommentCreateView.as_view(), name='shop_comment'),
    path('blogs/<int:pk>/', BlogsDetailView.as_view(), name='blog_detail'),
    path('<int:pk>/blog-comment/', CommentCreateView.as_view(), name='blog_comment'),
    path('blog/', BlogListView.as_view(), name='blog'),
]



