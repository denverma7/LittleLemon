from django.conf import settings
from django.test import SimpleTestCase
from rest_framework.routers import DefaultRouter

from .views import BookingsViewSet


class BookingRouterTests(SimpleTestCase):
    def test_booking_viewset_registers_with_router(self):
        router = DefaultRouter()
        router.register(r'tables', BookingsViewSet)

        routes = [str(pattern.pattern) for pattern in router.urls]
        self.assertTrue(any('tables' in route for route in routes))


class AuthConfigurationTests(SimpleTestCase):
    def test_rest_framework_supports_bearer_jwt_and_token_auth(self):
        self.assertIn('rest_framework.authentication.TokenAuthentication',
                      settings.REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'])
        self.assertIn('rest_framework_simplejwt.authentication.JWTAuthentication',
                      settings.REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'])


class MenuItemSerializerTests(SimpleTestCase):
    def test_serializer_uses_real_model_field_names(self):
        from LittleLemonAPI.models import MenuItem
        from LittleLemonAPI.serializers import MenuItemSerializer

        field_names = set(MenuItemSerializer().fields.keys())
        self.assertTrue({'ID', 'Title', 'Price', 'Inventory'}.issubset(field_names))
