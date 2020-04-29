from django.conf.urls import url, include
from django.conf.urls.i18n import i18n_patterns
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
    path('nk-admin/', admin.site.urls),
    path('markdownx/', include('markdownx.urls')),

    path('robots\.txt', TemplateView.as_view(
        template_name="config/robots.txt", content_type='text/plain')),
]

urlpatterns += i18n_patterns(
    path('', include('blog.urls')),
    path('api/1.0/', include(api_urlpatterns)),
    path('contact/', blog_views.ContactView.as_view(
        template_name='static/contact.html'), name='contact'),
    path('feeds/', LatestEntriesFeed(), name='feeds'),
    prefix_default_language=False
)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
