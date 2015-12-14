from math import sqrt

p = 2

x = sqrt(p)
xn = [x]
limit = 20

for i in range(limit):
 xn.append(sqrt(p + xn[-1]))
 x = xn[-1]

[print(x) for x in xn]
print((1 + sqrt(1 + 4 * p)) / 2, (1 - sqrt(1 + 4 * p)) / 2)