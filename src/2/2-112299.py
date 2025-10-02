# https://informatics.msk.ru/mod/statements/view.php?chapterid=112299

input()
a = [int(i) for i in input().split()]
k, m = [int(i) - 1 for i in input().split()]
while k < m:
  a[k], a[m] = a[m], a[k]
  k += 1
  m -= 1
