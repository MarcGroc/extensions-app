# from django.contrib.auth import get_user_model
# from django.test import SimpleTestCase, TestCase
# from django.urls import resolve, reverse
# from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
#
# User = get_user_model()
#
#
# class UrlsTestCase(SimpleTestCase):
#     """ Test urls """
#
#     def test_api_schema_url_resolves(self):
#         url = reverse('api-schema')
#         self.assertEqual(resolve(url).func.view_class, SpectacularAPIView)
#
#     def test_api_docs_url_resolves(self):
#         url = reverse('api-docs')
#         self.assertEqual(resolve(url).func.view_class, SpectacularSwaggerView)
#
#
# class AccessUrlsTestCase(TestCase):
#
#     def setUp(self):
#         pass
#
#     def test_admin_access(self):
#         """Test, should return 302"""
#         url = reverse('admin:index')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 302)
#
#     def test_api_docs_access(self):
#         """Test, should return 403"""
#         url = reverse('api-docs')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 403)
