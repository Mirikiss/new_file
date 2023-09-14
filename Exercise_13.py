import decimal

names = ['Pavel', 'Sergei', 'Oleg']
rate = [10500, 15000, 20100]
premium = ['10%', '5%', '7%']

print({ names: rate * decimal.Decimal(premium[:-1]) for names, rate, premium in zip(names, rate, premium)})
