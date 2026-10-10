from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.

class MessagePageTests(SimpleTestCase):
    
    def test_url_exist_at_correct_location(self):
        response = self.client.get("/message/")
        self.assertEqual(response.status_code, 200)
        
    def test_url_available(self):
        response = self.client.get(reverse('message'))
        self.assertEqual(response.status_code, 200)
        
        
    def test_templat(self):
        response = self.client.get(reverse('message'))
        self.assertTemplateUsed(response, 'index.html')
        
    def test_templat_content(self):
        response = self.client.get('/message/')
        self.assertContains(response, '<h1>Mahdi</h1>')