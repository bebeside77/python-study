__author__ = 'may'

year_lists = [1980, 1981, 1982, 1983, 1984]
print(year_lists)
print(year_lists[2])
print(year_lists[-1])
print(year_lists[len(year_lists) - 1])

things = ['mozzarella', 'cinderella', 'salmonella']
print(things[0].capitalize())
print(things)
things[0] = things[0].capitalize()
print(things)

print(things[0].upper())
things.remove('salmonella')
print(things)

e2f = {'dog' : 'chien', 'cat' : 'chat', 'walrus' : 'morse'}
print(e2f)
print(e2f['walrus'])

f2e = dict()
for key, value in e2f.items():
    f2e[value] = key
print(f2e)
print(f2e['chien'])
print(list(e2f.keys()))

life = {'animals' : {'cats' : 'Henri', 'octopi' : 'Grumpy', 'emus' : 'Lucy'}, 'plants' : {}, 'other' : {}}
print(life)
print(list(life.keys())[0])
print(list(life['animals'].keys()))
print(life['animals']['cats'])
