
def combinations(items, n):
 if n == 0:
  yield []
 for i in range(len(items)):
  for result in combinations(items[i+1:], n - 1):
   yield [items[i]] + result

def permutations(items, n=-1):
 if len(items) == 0 or n == 0:
  yield []
 else:
  for i in range(len(items)):
   for remainder in permutations(items[:i] + items[i + 1:], n - 1):
    yield [items[i]] + remainder

def permutationsI(items):
 return
 
def combinationsI(items, n):
 return

print("Combinations:")
for c in combinations([1, 2, 3, 4], 2):
 print(c)

print("Permutations:")
for p in permutations(['d', 'd', 'r', 'r'], 4):
 print(p)
 
 ### https://docs.python.org/3/library/itertools.html#itertools.combinations