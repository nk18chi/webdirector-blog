from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

from blog.feeds import LatestEntriesFeed
from blog import views as blog_views

urlpatterns = [
    url(r'^$', blog_views.TopView.as_view(), name='top'),
    url(r'^nk-admin/', admin.site.urls),

    url(r'^privacy/', TemplateView.as_view(template_name="static/privacy.html"), name='privacy'),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^contact/$', blog_views.ContactView.as_view(template_name='contact.html'), name='contact'),
    url(r'^contact/finish/$', TemplateView.as_view(template_name='contact_finish.html')),
    url(r'^contact/finish/sp/$',
        TemplateView.as_view(template_name='sp/contact_finish.html')),
    url(r'^feeds/$', LatestEntriesFeed(), name='feeds'),

    url(r'^', include('blog.urls', namespace='blog')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
