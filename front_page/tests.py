from django.test import SimpleTestCase


class HomePageTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_home_contains_correct_html(self):
        response = self.client.get("/")
        self.assertContains(response, "<h1>The Excursion Club UCSB</h1>")
