from django.conf.urls import url
from django.views.generic import TemplateView
from . import views
from blog.feeds import LatestEntriesFeed

app_name = "blog"

urlpatterns = [
    url(r'^$', views.TopView.as_view(), name='top'),
    url(r'^t_(?P<tag_id>[0-9]+)/$', views.TagListView.as_view(), name='tag_search'),
    url(r'^c_(?P<category_id>[0-9]+)/$', views.CategoryListView.as_view(), name='category_search'),
    url(r'^c_(?P<category_id>[0-9]+)/p_(?P<pk>[0-9]+)/$', views.BlogPostView.as_view(), name='post_detail'),
    url(r'^about/$', views.AboutPostView.as_view(template_name='about.html'), name='about'),
    url(r'^contact/$', views.ContactView.as_view(template_name='contact.html'), name='contact'),
    url(r'^contact/finish/$', TemplateView.as_view(template_name='contact_finish.html')),
    url(r'^contact/finish/sp/$', TemplateView.as_view(template_name='sp/contact_finish.html')),
    url(r'^feeds/$', LatestEntriesFeed(), name='feeds'),
]