from django.conf import urls
from exampleproject.exampleapp import views
from rest_framework import routers


router = routers.DefaultRouter()


urlpatterns = [] + router.urls
