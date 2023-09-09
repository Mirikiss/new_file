file = 'Жил себе дед да баба, у них была курочка Ряба; снесла под полом яичко — пестро, востро, костяно, мудрено! Дед бил — не разбил, баба била — не разбила, а мышка прибежала да хвостиком раздавила. Дед плачет, баба плачет, курочка кудкудачет, ворота скрипят, со двора щепки летят, на избе верх шатается!'.replace(',', '').replace('!','').replace('.','').replace('—','')

lists_file = file.split()

dict_file = {}

for i in lists_file:
    dict_file[i] = dict_file.get(i, 0) + 1

new_list = sorted(dict_file.items(), key=lambda para: (para[1], para[0]), reverse=True)[:10]

for i, w in enumerate(new_list, 1):
        print(f"{i:2}. {w[0]:<10} - {w[1]}")