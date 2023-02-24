#!/usr/bin/python3
"""Test for place classes"""
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
import pep8
import unittest


class Testplace(unittest.TestCase):
    """Unittests for testing the Place class"""

    def test_pep8_conform_place(self):
        """Test if we conform to PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_class(self):
        """Tests if class is named correctly"""
        place1 = Place()
        self.assertEqual(place1.__class__.__name__, "Place")

    def test_mother(self):
        """Tests if Class inherits from BaseModel"""
        place1 = Place()
        self.assertTrue(issubclass(place1.__class__, BaseModel))
