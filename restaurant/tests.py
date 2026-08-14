from django.test import SimpleTestCase
from rest_framework.routers import DefaultRouter

from .views import BookingsViewSet


class BookingRouterTests(SimpleTestCase):
    def test_booking_viewset_registers_with_router(self):
        router = DefaultRouter()
        router.register(r'tables', BookingsViewSet)

        routes = [pattern.pattern for pattern in router.urls]
        self.assertIn('tables/', routes)
