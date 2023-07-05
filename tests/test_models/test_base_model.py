#!/usr/bin.python3
'''xclkfjhbwldik fubhnwd lkufn u'''


import unittest
import uuid
import datetime
import time
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    '''UNITTEST DE LA CLASSE BASEMODEL'''

    def setUp(self):
        self.model = BaseModel()

    def test_id_is_valid_uuid(self):
        '''Vérifie si l'ID généré est un UUID valide'''
        self.assertTrue(uuid.UUID(self.model.id, version=4))

    def test_created_at_is_datetime(self):
        '''Vérifie si created_at est un objet datetime'''
        self.assertIsInstance(self.model.created_at, datetime.datetime)

    def test_updated_at_is_datetime(self):
        '''Vérifie si updated_at est un objet datetime'''
        self.assertIsInstance(self.model.updated_at, datetime.datetime)

    def test_save_updates_updated_at(self):
        '''Vérifie si la méthode save met à jour updated_at'''
        previous_updated_at = self.model.updated_at
        '''Attente d'une seconde pouorodatages'''
        time.sleep(1)
        self.model.save()
        self.assertNotEqual(previous_updated_at, self.model.updated_at)

    def test_to_dict_returns_dict(self):
        '''Vérifie si to_dict() retourne un dictionnaire'''
        result = self.model.to_dict()
        self.assertIsInstance(result, dict)

    def test_to_dict_contains_required_keys(self):
        '''Vérifie si to_dict() renvoiet les clés requises'''
        result = self.model.to_dict()
        required_keys = ["id", "__class__", "created_at", "updated_at"]
        for key in required_keys:
            self.assertIn(key, result)

    def test_str_returns_string(self):
        '''Vérifie si __str__() retourne une chaîne de caractères'''
        result = str(self.model)
        self.assertIsInstance(result, str)


if __name__ == '__main__':
    unittest.main()
