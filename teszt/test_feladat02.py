from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TestSzokoev(TestCase):
    def test_feladat01(self):
        aktualis = feladatok.csokkeno(1,2,3)
        elvart = [3,2,1]
        self.assertEqual(elvart, aktualis, "A sorrendet nem jól határozta meg")
    def test_feladat02(self):
        aktualis = feladatok.csokkeno(1,3,2)
        elvart = [3,2,1]
        self.assertEqual(elvart, aktualis, "A sorrendet nem jól határozta meg")
    def test_feladat03(self):
        aktualis = feladatok.csokkeno(2,3,1)
        elvart = [3,2,1]
        self.assertEqual(elvart, aktualis, "A sorrendet nem jól határozta meg")
    def test_feladat04(self):
        aktualis = feladatok.csokkeno(2,1,3)
        elvart = [3,2,1]
        self.assertEqual(elvart, aktualis, "A sorrendet nem jól határozta meg")
    def test_feladat05(self):
        aktualis = feladatok.csokkeno(3,2,1)
        elvart = [3,2,1]
        self.assertEqual(elvart, aktualis, "A sorrendet nem jól határozta meg")
    def test_feladat06(self):
        aktualis = feladatok.csokkeno(3,1,2)
        elvart = [3,2,1]
        self.assertEqual(elvart, aktualis, "A sorrendet nem jól határozta meg")

