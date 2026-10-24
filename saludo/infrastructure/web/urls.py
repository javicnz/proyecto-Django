from django.urls import path

from saludo.infrastructure.web.views import home


urlpatterns = [path("", home, name="home")]