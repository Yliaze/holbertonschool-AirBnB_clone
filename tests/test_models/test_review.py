import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    def test_class(self):
        classe = Review()
        self.assertEqual(classe.place_id, "")
        
        