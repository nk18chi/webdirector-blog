from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView
from . import views


app_name = "blog"

urlpatterns = [
    path('', views.TopView.as_view(), name='top'),
    url(r'^t_(?P<tag_id>[0-9]+)/$',
        views.TagListView.as_view(), name='tag_search'),
    url(r'^c_(?P<category_id>[0-9]+)/$',
        views.CategoryListView.as_view(), name='category_search'),
    url(r'^c_(?P<category_id>[0-9]+)/p_(?P<pk>[0-9]+)/$',
        views.BlogPostView.as_view(), name='post_detail'),
]
