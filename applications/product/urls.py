
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from applications.product.views import CategoryView, ProductView, CommentCreateView

router = DefaultRouter()
router.register('category', CategoryView)
router.register('comment',CommentCreateView)
router.register('', ProductView)
# router.register('comment',CommentCreateView)

urlpatterns = [
    # path('category/', CategoryView.as_view({'get': 'list'}))
    path('', include(router.urls)),
    # path('comment/', CommentCreateView.as_view({'get': 'list'}))
]
