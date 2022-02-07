from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TestNegyzetszamok(TestCase):
    def test_feladat01(self):
        aktualis = feladatok.negyzetszamok_szama(1,9)
        elvart = 3
        self.assertEqual(elvart, aktualis, "Nem minden intervallaum esetén határozta meg helyesen az intervallumba eső négyzetszámok számát!")

    def test_feladat02(self):
        aktualis = feladatok.negyzetszamok_szama(10,30)
        elvart = 2
        self.assertEqual(elvart, aktualis, "Nem minden intervallaum esetén határozta meg helyesen az intervallumba eső négyzetszámok számát!")

    def test_feladat03(self):
        aktualis = feladatok.negyzetszamok_szama(37,48)
        elvart = 0
        self.assertEqual(elvart, aktualis, "Nem minden intervallaum esetén határozta meg helyesen az intervallumba eső négyzetszámok számát!")

    def test_feladat04(self):
        aktualis = feladatok.negyzetszamok_szama(25,49)
        elvart = 3
        self.assertEqual(elvart, aktualis, "Nem minden intervallaum esetén határozta meg helyesen az intervallumba eső négyzetszámok számát!")

    def test_feladat05(self):
        aktualis = feladatok.negyzetszamok_szama(100,400)
        elvart = 11
        self.assertEqual(elvart, aktualis, "Nem minden intervallaum esetén határozta meg helyesen az intervallumba eső négyzetszámok számát!")

    def test_feladat06(self):
        aktualis = feladatok.negyzetszamok_szama(401,1601)
        elvart = 20
        self.assertEqual(elvart, aktualis, "Nem minden intervallaum esetén határozta meg helyesen az intervallumba eső négyzetszámok számát!")

    def test_feladat07(self):
        aktualis = feladatok.negyzetszamok_szama(2402,2499)
        elvart = 0
        self.assertEqual(elvart, aktualis, "Nem minden intervallaum esetén határozta meg helyesen az intervallumba eső négyzetszámok számát!")



