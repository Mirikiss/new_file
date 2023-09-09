# Задание №5
# ✔ Функция принимает на вход три списка одинаковой длины:
# ✔ имена str,
# ✔ ставка int,
# ✔ премия str с указанием процентов вида «10.25%».
# ✔ Вернуть словарь с именем в качестве ключа и суммой
# премии в качестве значения.
# ✔ Сумма рассчитывается как ставка умноженная на процент премии. 


def price(names, rate, premium):
    s = {}
    for name, r, p in zip(names, rate, premium):
        p = float(p[:-1])/100
        s[name] = r * p
    return s



names = ['Pavel', 'Sergei', 'Oleg']
rate = [10500, 15000, 20100]
premium = ['10%', '5%', '7%']

print(price(names, rate, premium))

