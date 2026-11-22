import unittest
from tuote import Tuote

class TestTuote(unittest.TestCase):
    def setUp(self):
        self.tuote = Tuote(1, "maito", 5)

    def test_tuote_attribuutit(self):
        self.assertEqual(self.tuote.id, 1)
        self.assertEqual(self.tuote.nimi, "maito")
        self.assertEqual(self.tuote.hinta, 5)

    def test_hash(self):
        self.assertEqual(hash(self.tuote), hash(1))

    def test_samat_tuotteet(self):
        toinen = Tuote(1, "eri nimi", 99)
        self.assertEqual(self.tuote, toinen)

    def test_erilaiset_tuotteet(self):
        toinen = Tuote(2, "leipa", 10)
        self.assertNotEqual(self.tuote, toinen)

    def test_str(self):
        self.assertEqual(str(self.tuote), "maito")