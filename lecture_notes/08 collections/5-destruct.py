getFirstAndLast = lambda array: (array[0], array[-1])

def _print(ages):
    first, last = getFirstAndLast(ages)
    print('\n'+'ages:', ages)
    print('first:', first, ', last:', last)
    return


schoolAges = [10, 12, 15, 15]
studentAges = [17, 18, 18, 19, 20]
ages = [*schoolAges,*studentAges]
_print(ages)

# splitting the list using a filter
schoolAges_2 = list(filter(lambda x: x < 17, ages))
_print(schoolAges_2)
studentAges_2 = list(filter(lambda x: x >= 17, ages))
_print(studentAges_2)

