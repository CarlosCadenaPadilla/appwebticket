from django.contrib import admin
from django.urls import path, include
from events.urls import events_patterns
from django.conf import settings

urlpatterns = [
    path('', include('core.urls')),
    path('', include(events_patterns)),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)