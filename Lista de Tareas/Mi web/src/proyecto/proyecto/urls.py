"""
URL configuration for proyecto project.
...
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("base.urls")),
]

# Servir ficheros estáticos solo en desarrollo (DEBUG=True)
if settings.DEBUG:
    # document_root: preferimos STATICFILES_DIRS[0] si está definido,
    # si no, usar STATIC_ROOT (aunque en dev normalmente usamos STATICFILES_DIRS)
    doc_root = None
    if getattr(settings, "STATICFILES_DIRS", None):
        doc_root = settings.STATICFILES_DIRS[0]
    else:
        doc_root = settings.STATIC_ROOT
    urlpatterns += static(settings.STATIC_URL, document_root=doc_root)
