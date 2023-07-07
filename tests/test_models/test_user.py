#!/usr/bin/python3
""" Module for BaseModel unit tests """
import unittest
from models.user import User

class TestUser(unittest.TestCase):
    def test_email(self):
        classe = User()
        self.assertEqual(classe.email, "")
        
    def test_password(self):
        classe = User()
        self.assertEqual(classe.password, "")
    
    def test_first_name(self):
        classe = User()
        self.assertEqual(classe.first_name, "")
        
    def test_last_name(self):
        classe = User()
        self.assertEqual(classe.last_name, "")
