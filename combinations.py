
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

def permutationsI(items, k=-1):
 pool = tuple(items)
 N = len(pool)
 k = N if k == -1 else k
 indices = list(range(N))
 cycles = list(range(N, N - k, -1))
 yield tuple(pool[i] for i in indices[:k])
 
 while N:
  for i in reversed(range(k)):
   cycles[i] -= 1
   if cycles[i] == 0:
    indices[i:] = indices[i + 1:] + indices[i:i + 1]
    cycles[i] = N - i
   else:
    j = cycles[i]
    indices[i], indices[-j] = indices[-j], indices[i]
    yield tuple(pool[i] for i in indices[:k])
    break
  else:
   return
 
def combinationsI(items, k):
 pool = tuple(items) # use tuple (immutable) instead of list (mutable) for speed
 N = len(pool)
 indices = list(range(k)) # indices will be modified below
 yield tuple(pool[i] for i in indices)
 
 while True:
  for i in reversed(range(k)):
   if indices[i] != i + N - k:
    break
  else:
   return
  indices[i] += 1
  for j in range(i + 1, k):
   indices[j] = indices[j - 1] + 1
  yield tuple(items[i] for i in indices)

print("Combinations (recursive):")
for c in combinations([1, 2, 3, 4], 2):
 print(c)

print("Combinations (iterative):")
for c in combinationsI([1, 2, 3, 4], 2):
 print(c)

print("Permutations (recursive):")
for p in permutations([1, 2, 3, 4], 2):
 print(p)

print("Permutations (iterative):")
for p in permutationsI([1, 2, 3, 4], 2):
 print(p)

