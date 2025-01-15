from rest_framework.routers import SimpleRouter

from market.views import SupplierViewSet
from market.apps import MarketConfig

app_name = MarketConfig.name

router = SimpleRouter()
router.register('', SupplierViewSet)

urlpatterns = []

urlpatterns += router.urls
