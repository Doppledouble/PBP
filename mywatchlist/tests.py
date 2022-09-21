from django.test import TestCase

class testurls(TestCase):
    def test_html(self):
        response = self.client.get("/mywatchlist/html/")
        self.assertEquals(response.status_code,200)
        
    def test_json(self):
        response = self.client.get("/mywatchlist/json/")
        self.assertEquals(response.status_code,200)

    def test_xml(self):
        response = self.client.get("/mywatchlist/xml/")
        self.assertEquals(response.status_code,200)
  
        # Create your tests here.
