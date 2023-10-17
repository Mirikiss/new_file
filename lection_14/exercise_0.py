

def is_prime(p):
    '''
    >>> is_prime(43)
    False
    >>> is_prime(73)
    True
    >>> is_prime(100_000_002)
    False
    '''
    if not isinstance(p, int):
        raise TypeError('Error')
    elif p < 2:
        raise ValueError('Error')
    elif p > 100_000_000:
        print('BIG')
    for i in range(2, p):
        if p % i == 0:
            return False
        return True

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)


#print(is_prime(73))