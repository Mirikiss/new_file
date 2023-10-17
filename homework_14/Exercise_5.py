# На семинаре 13 был создан проект по работе с пользователями (имя, id, уровень).
# Напишите 3-7 тестов pytest для данного проекта.
# Используйте фикстуры.

from homework_14 import *

import pytest

@pytest.fixture
def data():
    return Company('N')

def test1(data):     
    assert data.login('Астапович Евгений Петрович','851237')

def test2(data):     
    with pytest.raises(Exception):
        assert data.login('Астапович Евгений Петрович','851237')

def test3(data):     
    with pytest.raises(Exception):
        assert data.login('Астапович Евгений Петрович','851237')==('Астапович Евгений Петрович','851237',5) 

def test4(data):                      
    with pytest.raises(LevelError):
        me=data.login('Владимир Владимир Николаевич','038684') 
        n.hiring(me,'Смернов Павел','111211',3)  

if __name__ == '__main__':
    pytest.main(['-v'])