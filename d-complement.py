# 'use strict';
# const difference = (s1, s2) => {
#  const ds = [];
#  for (let i = 0; i < s1.length; i++) {
#    const item = s1[i];
#    if (!s2.includes(item)) ds.push(item);
#  }
#  return ds;
# };

#// const difference = (s1, s2) => new Set(
#//   [...s1].filter((v) => !s2.has(v))
#// );

# const complement = (s1, s2) => difference(s2, s1);

#// Usage

# const cities1 = ['Beijing', 'Kiev'];
# const cities2 = ['Kiev', 'London', 'Baghdad'];
# console.dir({ cities1, cities2 });
# const results = complement(cities1, cities2);
# console.dir(results);

# ---------------------------------------------------------------

cities1 = ['Beijing', 'Kiev']
cities2 = ['Kiev', 'London', 'Baghdad']
print('cities1:', cities1)
print('cities2:', cities2)

results = [] + [x for x in cities2 if not x in cities1]
print('complement = (cities1, cities2) => difference(cities2, cities1)')
print('complement:', results)