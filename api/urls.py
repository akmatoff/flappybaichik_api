from rest_framework import routers
from django.urls import path
from .views import RecordViewSet

router = routers.DefaultRouter()
router.register('records', RecordViewSet, 'records')

urlpatterns = router.urls