
def fib(n):
 if n == 0:
  return 0
 elif n == 1:
  return 1
 else:
  return fib(n - 1) + fib(n - 2)

def fibi(n):
 old, new = 0, 1
 if n == 0:
  return 0
 for i in range(n - 1):
  old, new = new, old + new
 return new

memo = {0:0, 1:1}
def fibm(n):
 if not n in memo:
  memo[n] = fibm(n - 1) + fibm(n - 2)
 return memo[n]

import timeit

for i in range(1, 31):
 s = "fib(" + str(i) + ")"
 time1 = timeit.timeit(s, setup="from __main__ import fib", number=3)
 s = "fibi(" + str(i) + ")"
 time2 = timeit.timeit(s, setup="from __main__ import fibi", number=3)
 s = "fibm(" + str(i) + ")"
 time3 = timeit.timeit(s, setup="from __main__ import fibm", number=3)
 print("n=%2d, fib: %8.6f, fibi: %7.6f, fibm: %7.6f" % (i, time1, time2, time3))

