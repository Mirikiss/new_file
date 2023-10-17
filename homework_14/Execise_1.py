# 📌 На семинаре 13 был создан проект по работе с пользователями (имя, id, уровень)
# 📌 Напишите 3-7 тестов pytest (или unittest на ваш выбор) для данного проекта
# 📌 ОБЯЗАТЕЛЬНО! Используйте фикстуры


from seminar_13.Exercise_4 import Worker

from Seminar_14.Semin13_Task5 import UserWorkshop, User
from Seminar_14.Exceptions import AccesErorr, LevelError
from Seminar_14.Semin13_User import User

import pytest

@pytest.fixture
def SetUp():
    return Worker()

def test_file_1(SetUp):
    with pytest.raises(AccesError, match='Access denied'):
        SetUp.login('Nevsterovs, 1')

def test_access(SetUp):
    assert SetUp.login('Nevsterovs, 1') == '5'

def test_file_2(SetUp):
    with pytest.raises(LevelError):
        SetUp.login('Nesterov', '1')
        SetUp.create_user('New_user', '1', '3')

if __name__ == '__main__':
    pytest.main(['-v'])