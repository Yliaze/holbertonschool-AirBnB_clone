import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    def test_class(self):
        classe = Place()
        self.assertEqual(classe.name, "")
        
        