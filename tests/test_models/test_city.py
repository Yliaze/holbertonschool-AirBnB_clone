import unittest
from models.city import City

class TestCity(unittest.TestCase):
    def test_class(self):
        classe = City()
        self.assertEqual(classe.name, "")
        
        