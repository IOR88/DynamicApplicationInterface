"""exampleproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from django.views import generic
from exampleproject.views import BaseView
from exampleproject.exampleapp import urls as exampleapp_urls
from rest_framework import permissions

schema_view = get_schema_view(
    title='Example Project API',
    urlconf='exampleproject.exampleapp.urls',
    permission_classes=[permissions.AllowAny]
)

urlpatterns = [
    path(r'', BaseView.as_view()),
    path('admin/', admin.site.urls),
    path('api/exampleapp/', include(exampleapp_urls)),
    path(r'', generic.base.RedirectView.as_view(
        pattern_name='',
        url='/',
        permanent=True
    )),
    path('schema/openapi', schema_view, name='schema-openapi')
]

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
