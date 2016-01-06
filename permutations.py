
myItems = ['a', 'b', 'c', 'd']

def permutationsR(items):
 """ yields all permutations of a set """
 if len(items) == 0:
  yield []
 for i in range(len(items)):
  for remainder in permutationsR(items[:i] + items[i+1:]):
   yield [items[i]] + remainder

def permutationsR2(items):
 if len(items) == 0:
  yield []
 for item in items:
  for remainder in permutationsR2([otherItems for otherItems in items if item not in otherItems]):
   yield [item] + remainder

def permutationsI(items):
  a = items[:]
  N = len(a)
  p = [n for n in range(N + 1)]
  i = 1
  yield a
  while i < N:
    p[i] -= 1
    j = (i % 2) * p[i]
    a[j], a[i] = a[i], a[j]
    yield a
    i = 1
    while p[i] == 0:
      p[i] = i
      i += 1

def permutationsI2(items):
  a = items[:]
  N = len(a)
  p = [0 for n in range(N)]
  i = 1
  yield a
  while i < N:
    if p[i] < i:
      j = (i % 2) * p[i]
      a[j], a[i] = a[i], a[j]
      yield a
      p[i] += 1
      i = 1
    else:
      p[i] = 0
      i += 1

from timeit import timeit
t1 = timeit("for x in permutationsR(['a', 'b', 'c', 'd', 'e', 'f']): pass", setup="from __main__ import permutationsR", number=500)
t2 = timeit("for x in permutationsI(['a', 'b', 'c', 'd', 'e', 'f']): pass", setup="from __main__ import permutationsI", number=500)
t3 = timeit("for x in permutationsI2(['a', 'b', 'c', 'd', 'e', 'f']): pass", setup="from __main__ import permutationsI2", number=500)
t4 = timeit("for x in permutationsI2(['a', 'b', 'c', 'd', 'e', 'f', 'g']): pass", setup="from __main__ import permutationsI2", number=500)
t5 = timeit("for x in permutationsR2(['a', 'b', 'c', 'd', 'e', 'f']): pass", setup="from __main__ import permutationsR2", number=500)
print("Recursive method: %0.6f" % t1)
print("Recursive method list comprehension: %0.6f" % t5)
print("Iterative countdown: %0.6f" % t2)
print("Iterative counting: %0.6f" % t3)
print("Longer Iterative counting: %0.6f" % (t4 / t3))

"""
print('recursive:')
for x in permutationsR(['a', 'b', 'c']):
 print(x)

print('recursive list comprehension:')
for x in permutationsR2(['a', 'b', 'c']):
 print(x)

print('countdown:')
for x in permutationsI(['a', 'b', 'c']):
 print(x)

print('counting:')
for x in permutationsI2(['a', 'b', 'c']):
 print(x)
"""