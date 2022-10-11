from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter

from .views import run_calculator
from .api import MortgageOffersViewSet


router = DefaultRouter()
router.register('', MortgageOffersViewSet)


urlpatterns = [
    path('api/offer/', include(router.urls)),
    path('', run_calculator, name='calculator'),
]
