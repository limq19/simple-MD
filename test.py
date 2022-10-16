import numpy as np
# import json
# f = open('INPUT.json', 'r')
# load = json.load(f)
# print(type(load))
position = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
box = [3, 4, 5]
xr = position - box * np.rint(position / box)
print(xr)
