from rest_framework.routers import DefaultRouter
from ..views.order_views import WorkOrderViewset
from ..views.products_views import ProductsViewset
router = DefaultRouter()
router.register('workorder', WorkOrderViewset, basename="work_order")
router.register('products', ProductsViewset, basename="products")
urlpatterns = router.urls