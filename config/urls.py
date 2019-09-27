from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^nk-admin/', admin.site.urls),
    url(r'^', include('blog.urls', namespace='blog')),
    url('markdownx/', include('markdownx.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
