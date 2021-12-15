cache = {}  # dictionary

def addProcedure(a, b):
    key = [str(a) + ',' + str(b)]
    if cache == {}:
        res = cache.fromkeys(key)  # create a dictionary with a key
    else:
        res = cache
    if res.get(key) != None:
        return res.get(key)  # returns the value of the key, but if there is none, then None
    res = a + b
    cache[key] = res
    return res


def subProcedure(a, b):
    key = [str(a) + ',' + str(b)]
    if cache == {}:
        res = cache.fromkeys(key)  # create a dictionary with a key
    else:
        res = cache
    if res.get(key) != None:
        return res.get(key)  # returns the value of the key, but if there is none, then None
    res = a - b
    cache[key] = res
    return res



print('sub:', subProcedure(5, 2))  # result = 5-2 = 3; written to cache, key = 5,2 result = 3
print('add:', addProcedure(5, 2))  # result = 3, took the result from the cache for key 5,2
