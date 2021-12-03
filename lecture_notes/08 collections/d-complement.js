cities1 = ['Beijing', 'Kiev']
cities2 = ['Kiev', 'London', 'Baghdad']
print('cities1:', cities1)
print('cities2:', cities2)

results = [] + [x for x in cities2 if not x in cities1]
print('complement = (cities1, cities2) => difference(cities2, cities1)')
print('complement:', results)
