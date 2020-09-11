from django.conf import urls
from exampleproject.exampleapp import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'^categories', views.CategorySetView)
router.register(r'^items', views.ItemSetView)

urlpatterns = [] + router.urls
