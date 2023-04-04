import numpy as np

a = [[1,2,3],[4,5,6],[7,8,9]]
b = [[3,2,1],[0,3,2],[4,3,1]]

a = np.array(a)
b = np.array(b)
c = np.dot(a,b)

print(str(c).replace("[", " ").replace("]", " ").replace("  ", " ").replace(" ", "   "))