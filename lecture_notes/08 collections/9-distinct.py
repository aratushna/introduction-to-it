flights_from = ['Kiev', 'Kiev', 'Dublin', 'Riga', 'Kiev', 'Cairo']
flights_to = ['Rome', 'Warsaw', 'Riga', 'Dublin', 'Rome', 'Paris']
flights = [flights_from[x] + ' >> ' + flights_to[x] for x in range(len(flights_from))]
print('flights :', '\n', flights)
directions = list(dict.fromkeys(flights))
print('directions :', '\n', directions)


