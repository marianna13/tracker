# Make sure the server is running and the database is empty for this test to work

from tracker import Tracker
import unittest

demo_url = "https://www.website.demo/section/media/service/cat-with-funny-face.jpg"

class TestStringMethods(unittest.TestCase):

    def test_tracker(self):
        client = Tracker('http://127.0.0.1:8000/')
        self.assertTrue(client.add(item=demo_url, status='processing'))
        self.assertTrue(client.get_item(demo_url))

        item = client.get_all_items()[0]
        self.assertEqual(item["id"], demo_url)
        self.assertEqual(item["status"], "processing")
        
        client.update(item=demo_url, status='completed')
        item = client.get_all_items()[0]
        self.assertEqual(item["id"], demo_url)
        self.assertEqual(item["status"], "completed")
        
        self.assertTrue(client.delete(item=demo_url))
        self.assertEqual(len(client.get_all_items()), 0)

if __name__ == '__main__':
    unittest.main()

