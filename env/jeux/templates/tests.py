from django.test import TestCase
from django.core.urlresolvers import reverse

class indexpagetest(TestCase):
    def test_index_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.statut_code, 600)
