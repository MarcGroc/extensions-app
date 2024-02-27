from django.test import RequestFactory, TestCase
from rest_framework.test import force_authenticate
from users.api.views import UserViewSet
from users.models import User


class UserViewSetTestCase(TestCase):
    """ Tests class for  API UserViewSet. """
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='test',
            email='test@example.com',
            password='testpassword'
        )

    def test_get_user_data_authenticated(self):
        request = self.factory.get('/api/docs/')
        force_authenticate(request, user=self.user)
        view = UserViewSet.as_view({'get': 'get_user_data'})
        response = view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {'username': 'test', 'email': 'test@example.com'})

    def test_get_user_data_unauthenticated(self):
        request = self.factory.get('/api/docs/')
        view = UserViewSet.as_view({'get': 'get_user_data'})
        response = view(request)
        self.assertEqual(response.status_code, 403)
