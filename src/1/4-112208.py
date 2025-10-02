# https://informatics.msk.ru/mod/statements/view.php?chapterid=112208

a, b = map(int, input().split())
c, d = map(int, input().split())

result = []
for i in range(10000, 99999 + 1):
    if i % a == b and i % c == d:
        result.append(i)

if len(result) == 0:
    print(-1)
else:
    print(*result)
