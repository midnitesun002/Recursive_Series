
fn = [1, 1]
limit = 25
for i in range(limit):
 fn.append(fn[-1] + fn[-2])

[print(xn1 / xn) for xn, xn1 in zip(fn, fn[1:])]