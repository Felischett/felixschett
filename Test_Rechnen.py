import unittest
from rechnen import addiere, dividiere

class TestRechner(unittest.TestCase):

    def test_addiere(self):
        self.assertEqual(addiere(2,3), 5)
        self.assertEqual(addiere(5,5), 10)

    def test_dividiere(self):
        self.assertEqual(dividiere(5,5),1)
        self.assertEqual(dividiere(10,5), 2)

    def test_dividiere_durch_null(self):
        with self.assertRaises(ValueError):
            dividiere(5,0)

if __name__ == "__main__":
    unittest.main()