# Задание №3
# Напишите для задачи 1 тесты unittest. Проверьте
# следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери
# символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов
# (кроме п. 1)

import unittest
from Exercise_1 import clear_case

class TestUnitMy(unittest.TestCase):

    def setUp(self):
        self.correct = 'text'
        self.first = 'TexT'
        self.second = 'Te..xt'
        self.third = 'TeAAxt'
        self.fourth = 'Te..AA..xt'
        
    def test1(self):
        self.assertEqual(self.correct, clear_case(self.first))

    def test2(self):
        self.assertTrue(self.correct == clear_case(self.first))
    
    def test4(self):
        self.assertRaises(ValueError, clear_case, None)


if __name__ == '__main__':
    unittest.main(verbosity=2)