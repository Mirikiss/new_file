import unittest

class TestSample(unittest.TestCase):

    def setUp(self):
        self.data = [2, 3, 4]
        print('asdas')
    
    def test_append(self):
        self.data.append(5)
        self.assertEqual(self.data, [2, 3, 4, 5])