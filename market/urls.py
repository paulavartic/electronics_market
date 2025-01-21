from django.urls import path
from rest_framework.routers import SimpleRouter

from market.views import SupplierViewSet, ProductViewSet, ChainUnitList, ChainUnitCreate, ChainUnitDetail
from market.apps import MarketConfig

app_name = MarketConfig.name

router = SimpleRouter()
router.register('', SupplierViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('chain-units/', ChainUnitList.as_view(), name='chain-unit-list'),
    path('chain-unit/create/', ChainUnitCreate.as_view(), name='chain-unit-create'),
    path('chain-unit/<int:pk>/', ChainUnitDetail.as_view(), name='chain-unit-detail'),
]

urlpatterns += router.urls
