import ast  # abstract syntax tree, conversion of code "{'x': 20,'y': 20}" >> {'x': 20,'y': 20}


def move(point):
    point['x'] += offset['x']
    point['y'] += offset['y']
    return point
# other version
# move = lambda point: {'x': point['x'] + offset['x'], 'y': point['y'] + offset['y']}

def conditionalParse(point):
    if str(type(point)) == "<class 'dict'>": return point  # type definition, translation to string
    return ast.literal_eval(point)  # returns a dictionary, "{'x': 20,'y': 20}" >> {'x': 20,'y': 20}


polyline = [
    {'x': 0, 'y': 0},
    {'x': 10, 'y': 10},
    "{'x': 20,'y': 20}",
    {'x': 30, 'y': 30},
]
print('polyline :', '\n', polyline)
offset = {'x': 10, 'y': -5}
polyline = list(map(conditionalParse, polyline))
path = list(map(move, polyline))
print('path :', '\n', path)
