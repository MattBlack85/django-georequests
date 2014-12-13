from django.contrib.auth.models import User
from django.contrib.auth.middleware import AuthenticationMiddleware
from django.contrib.sessions.middleware import SessionMiddleware
from django.core.exceptions import PermissionDenied
from django.test import TestCase
from django.test.client import RequestFactory

from djeorequests.middleware import GeoMiddleware

from .models import Visit
from .views import dashview


class BaseVisitTest(TestCase):

    def test_request_saved(self):
        request = RequestFactory(REMOTE_ADDR='173.194.113.110')
        request = request.get("/")

        self.assertEquals(Visit.objects.count(), 0)

        gm = GeoMiddleware()
        gm.process_request(request)

        self.assertEquals(Visit.objects.count(), 1)


class GeoDashboardBaseTest(TestCase):

    def setUp(self):
        request = RequestFactory()
        request = request.get("/")
        SessionMiddleware().process_request(request)
        AuthenticationMiddleware().process_request(request)
        self.request = request

    def test_403(self):
        with self.assertRaises(PermissionDenied):
            dashview(self.request)

    def test_method_not_allowed(self):
        self.request.method = "POST"
        self.request.user = User(is_superuser=True)
        resp = dashview(self.request)

        self.assertEquals(resp.status_code, 405)
