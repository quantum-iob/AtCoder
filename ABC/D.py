a = dict()
a[0] = 1
print(a)

x = list(range(100))
y = []
for i in enumerate(x, 0):
    y.append(list(i))

print(y)

y = sorted(y,key=lambda x: x[1], reverse=True)
y[1][1] += 1
print(y)
print(y[9][1] + 1)
print(y[1])[1]