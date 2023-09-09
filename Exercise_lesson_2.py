baggage = {
    'Denis': ('tent', 'meat', 'drink'),
    'Alex': ('tent', 'meat', 'drink'),
    'Vlad': ('tent', 'meat', 'wather')}

s = list(baggage.values())

bag_all = set()
bag_unique = set(s[0])

for i in s:
    bag_all = bag_all.union(set(i))
    bag_unique = bag_unique.intersection(set(i))

uniq_thing = {}
for name, items in baggage.items():
    uniq_thing[name] = set(items).difference(bag_unique)

uniq_thing_values = list(uniq_thing.values())
k =  [i for i in uniq_thing_values if uniq_thing_values.count(i) > 1]


print(f'Вещи которые они взяли {bag_all}')
print(f'Вещь которая есть только у одного {[i for i in uniq_thing_values if uniq_thing_values.count(i) == 1]}')
print(f'Вещи которые есть у вех кроме одно', *[i for i in uniq_thing_values if uniq_thing_values.count(i) > 1])
