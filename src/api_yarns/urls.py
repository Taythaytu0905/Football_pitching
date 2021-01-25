from rest_framework import routers

from api_yarns.views import YarnViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'yarn', YarnViewSet, basename="yarn")
urlpatterns = router.urls
