from django.test import TestCase, Client
from django.urls import reverse


client = Client()


class TestHomeView(TestCase):
    def test_should_return_200_when_home_is_called(self):
        expected_status_code = 200

        resp = client.get(reverse("home"))
        actual_status_code = resp.status_code

        self.assertEqual(actual_status_code, expected_status_code)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse("home"))

        self.assertTemplateUsed(resp, "main/base.html")
