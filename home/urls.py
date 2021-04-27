from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [ # Do not put underscore
    path("", views.index, name="index"), # ./ on route, run views.index
    path("institute-level-rsd", views.ilrsd, name="ilrsd"),
    path("department-level-rsd", views.dlrsd, name="dlrsd"),
    path("seminars", views.seminars, name="seminars"),
    path("links", views.links, name="links"),
    path("info", views.info, name="info"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)