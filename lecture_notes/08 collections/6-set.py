ages = [10, 12, 15, 15, 17, 18, 18, 19, 20]
print('original:', ages)
ages.append(16)
print('append:', ages)
ages.remove(20)
print('remove:', ages)

ages_keys= [10,16,19,20]
ages_values = [ages.__contains__(x) for x in ages_keys]
ages_dict = dict(zip(ages_keys, ages_values))
print('check:', ages_keys, '>>', ages_dict)

ages.clear()
print('clear:', ages)
