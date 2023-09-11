def kwargs_to_dict(**kwargs):
    result = {}
    for key, value in kwargs.items():
        try:
            result[value] = key
        except:
            result[str(value)] = key
    return result


print(kwargs_to_dict(name='Павел', sername='Заяц', weight=98.5,
                     months=['19', 'Апреля', '2023'],
                     courses={'python': '3.11', 'HTMl': '5'}))