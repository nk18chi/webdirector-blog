from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

from blog.feeds import LatestEntriesFeed
from blog import views as blog_views
from blog.api.urls import blogpost_router

api_urlpatterns = [
    path('blogposts/', include(blogpost_router.urls)),
]

urlpatterns = [
    url(r'^$', blog_views.TopView.as_view(), name='top'),
    url(r'^nk-admin/', admin.site.urls),
    url('markdownx/', include('markdownx.urls')),
    url(r'^api/1.0/', include(api_urlpatterns)),

    url(r'^contact/$', blog_views.ContactView.as_view(
        template_name='static/contact.html'), name='contact'),
    url(r'^feeds/$', LatestEntriesFeed(), name='feeds'),
    url(r'^robots\.txt$', TemplateView.as_view(
        template_name="config/robots.txt", content_type='text/plain')),
    url(r'^ads\.txt$', TemplateView.as_view(
        template_name="config/ads.txt", content_type='text/plain')),


    url(r'^', include('blog.urls', namespace='blog')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
