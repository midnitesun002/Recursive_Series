from math import sqrt

def nested(p):
 xn = sqrt(p)
 while True:
  yield xn
  xn = sqrt(p + xn)

count = 20
p = 2
for an in nested(p):
 print(an)
 count -= 1
 if count == 0:
  break

print('Limit: %0.18f' % ((1 + sqrt(1 + 4 * p)) / 2))