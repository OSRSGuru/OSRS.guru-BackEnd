from .api import ServerViewSet, GeographicalLocationViewSet, GameObjectViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'Servers', ServerViewSet)
router.register(r'ServerLocations', GeographicalLocationViewSet)
router.register(r'GameObjects', GameObjectViewSet)

urlpatterns = router.urls