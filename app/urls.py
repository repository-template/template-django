from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import AnimalViewSet

router = DefaultRouter()
router.register(r"animal", AnimalViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
# urlpatterns = [
#     path('model/', AnimalViewSet.as_view({'get': 'list'}), name='model'),  # Replace with your actual endpoint
# ]
