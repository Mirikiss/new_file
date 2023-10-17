from Exercise_1 import clear_case

import pytest

def test1():
    assert clear_case('te..xt') == 'text'

def test2():
    assert clear_case('Te//xt') == 'text'

def test2():
    assert clear_case('text') == 'text'

if __name__ == '__main__':
    pytest.main(['-v'])