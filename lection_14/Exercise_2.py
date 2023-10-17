# 📌Напишите для задачи 1 тесты unittest. Проверьте следующие варианты: 
# 📌возврат строки без изменений 
# 📌возврат строки с преобразованием регистра без потери символов 
# 📌возврат строки с удалением знаков пунктуации 
# 📌возврат строки с удалением букв других алфавитов 
# 📌возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)

import unittest

class TestUnitMy(unittest.TestCase):
    def setUp(self):
        self.correct = 'text'
        self.first = 'TexT'
        self.second = 'Te..xt'
        self.third = 'TeAAxt'
        self.fourth = 'Te..AA..xt'

    def test(self):
        self.assertEqual(self.correct, clear_text(self.first))