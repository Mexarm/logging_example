from django.test import TestCase
from django.test import Client
from django.urls import reverse


class TestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_view(self):
        reponse = self.client.get(reverse('logging'))
        self.assertEqual(reponse.status_code, 201,
                         "view should return 200 status code")
