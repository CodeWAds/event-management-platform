from django.contrib import admin
from django.urls import include, path

# эндпоинты страниц сайта
urlpatterns = [
    path("events/", include("events.urls")),
    path("admin/", admin.site.urls),
    path("auth_app/", include("auth_app.urls")),
]
