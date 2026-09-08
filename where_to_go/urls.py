from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from places.views import index, place_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path("places/<int:pk>/", place_detail, name="place_detail"),
    path('tinymce/', include('tinymce.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
