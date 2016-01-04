
def fib():
 n = 1
 xn1 = 1
 xn2 = 1
 while True:
  yield n, xn1
  n += 1
  next = xn1 + xn2
  xn1 = xn2
  xn2 = next

count = 20
print('  n:    fn')
for n, fn in fib():
 print('%3d: %5d' % (n, fn))
 if n > count:
  break