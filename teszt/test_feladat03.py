from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TestPalindrom(TestCase):
    def test_feladat01(self):
        aktualis = feladatok.palindrom_e("mm")
        elvart = True
        self.assertEqual(elvart, aktualis, "A palindrom_e függvény nem megfelelően működik!")

    def test_feladat02(self):
        aktualis = feladatok.palindrom_e("apa")
        elvart = True
        self.assertEqual(elvart, aktualis, "A palindrom_e függvény nem megfelelően működik!")

    def test_feladat03(self):
        aktualis = feladatok.palindrom_e("arcra")
        elvart = True
        self.assertEqual(elvart, aktualis, "A palindrom_e függvény nem megfelelően működik!")

    def test_feladat04(self):
        aktualis = feladatok.palindrom_e("kellek")
        elvart = True
        self.assertEqual(elvart, aktualis, "A palindrom_e függvény nem megfelelően működik!")

    def test_feladat05(self):
        aktualis = feladatok.palindrom_e("keretkarakterek")
        elvart = True
        self.assertEqual(elvart, aktualis, "A palindrom_e függvény nem megfelelően működik!")

    def test_feladat06(self):
        aktualis = feladatok.palindrom_e("te")
        elvart = False
        self.assertEqual(elvart, aktualis, "A palindrom_e függvény nem megfelelően működik!")

    def test_feladat07(self):
        aktualis = feladatok.palindrom_e("ima")
        elvart = False
        self.assertEqual(elvart, aktualis, "A palindrom_e függvény nem megfelelően működik!")

    def test_feladat08(self):
        aktualis = feladatok.palindrom_e("anya")
        elvart = False
        self.assertEqual(elvart, aktualis, "A palindrom_e függvény nem megfelelően működik!")

    def test_feladat09(self):
        aktualis = feladatok.palindrom_e("palindrom")
        elvart = False
        self.assertEqual(elvart, aktualis, "A palindrom_e függvény nem megfelelően működik!")


