"""Here we testing plateforme app templates"""

from django.test import TestCase
from django.urls import reverse


class indexpagetest(TestCase):
    """Here we testing"""

    def test_home_page(self):
        """test home template"""

        response = self.client.get(reverse('/templates/home'))
        self.assertEqual(response.status_code,200)
        

    def test_mention_page(self):
        """test mention page"""

        response = self.client.get(reverse('/templtates/mention'))
        self.assertEqual(response.status_code,200)
