from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TestSzokoev(TestCase):
    def test_feladat01(self):
        aktualis = feladatok.szokoev_e(1984)
        elvart = True
        self.assertEqual(elvart, aktualis, "A szökőévet nem jól határozta meg!")
    def test_feladat02(self):
        aktualis = feladatok.szokoev_e(1700)
        elvart = False
        self.assertEqual(elvart, aktualis, "A szökőévet nem jól határozta meg!")
    def test_feladat02(self):
        aktualis = feladatok.szokoev_e(1600)
        elvart = True
        self.assertEqual(elvart, aktualis, "A szökőévet nem jól határozta meg!")
