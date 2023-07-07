import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    def test_class(self):
        classe = Amenity()
        self.assertEqual(classe.name, "")
        