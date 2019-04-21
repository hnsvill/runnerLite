import unittest
from workoutCalculations import *


class test_prNks(unittest.TestCase):

    def test_prNks(self):
        self.assertEqual(prNks('6bd5f3c04e6b5279aca633c2a245dd9c', 5), 0)
        self.assertEqual(prNks('4e7aaa167b9b5ff7b9b3a22dee8c2085', 5), 0)
        self.assertEqual(prNks('c7e962db02da55209f02fe3d8a86c99d', 5), 2)
        self.assertEqual(prNks('d77908482ed2505ebbf17ef72be2f080', 5), 1)
        self.assertEqual(prNks('72eff89c74cc57178e02f103187ad579', 5), 0)
        self.assertEqual(prNks('40d7ae29e393582abdbcb8c726249e22', 5), 0)


class test_moreThanNkm(unittest.TestCase):

    def test_moreThanNkm(self):
        self.assertEqual(ranMoreThanNkm('6bd5f3c04e6b5279aca633c2a245dd9c', 10), 66)
        self.assertEqual(ranMoreThanNkm('4e7aaa167b9b5ff7b9b3a22dee8c2085', 10), 8)
        self.assertEqual(ranMoreThanNkm('c7e962db02da55209f02fe3d8a86c99d', 10), 3)
        self.assertEqual(ranMoreThanNkm('d77908482ed2505ebbf17ef72be2f080', 10), 10)
        self.assertEqual(ranMoreThanNkm('72eff89c74cc57178e02f103187ad579', 10), 61)
        self.assertEqual(ranMoreThanNkm('40d7ae29e393582abdbcb8c726249e22', 10), 0)


class test_greaterThanNkmStreaks(unittest.TestCase):

    def test_greaterThanNkmStreaks(self):
        self.assertEqual(greaterThanNkmStreaks('6bd5f3c04e6b5279aca633c2a245dd9c', 1, 3), 19)
        self.assertEqual(greaterThanNkmStreaks('4e7aaa167b9b5ff7b9b3a22dee8c2085', 1, 3), 5)
        self.assertEqual(greaterThanNkmStreaks('c7e962db02da55209f02fe3d8a86c99d', 1, 3), 3)
        self.assertEqual(greaterThanNkmStreaks('d77908482ed2505ebbf17ef72be2f080', 1, 3), 7)
        self.assertEqual(greaterThanNkmStreaks('72eff89c74cc57178e02f103187ad579', 1, 3), 21)
        self.assertEqual(greaterThanNkmStreaks('40d7ae29e393582abdbcb8c726249e22', 1, 3), 0)


if __name__ == '__main__':
    unittest.main()
