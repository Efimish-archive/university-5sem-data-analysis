x, y = map(float, input().split())

a = y <= 1
b = y <= -x
c = x**2 + y**2 <= 1
d = (x-1)**2 + y**2 <= 1

print(''.join('1' if i else '0' for i in [a, b, c, d]))
