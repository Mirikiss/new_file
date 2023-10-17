import unittest
from  seminar_10.Exercise_2 import Rectangle
class TestMy(unittest.TestCase):

    def setUp(self):
        self.ferst = Rectangle(2, 4)
        self.second = Rectangle(3, 7)

    def test1(self):
        self.assertTrue(self.ferst == self.second)
    
    def test2(self):
        self.assertNotEqual(self.ferst, self.second)

        





if __name__ == '__main__':
    unittest.main(verbosity=2)