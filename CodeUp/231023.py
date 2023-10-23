# 6071
n = int(input())
while n != 0:
    print(n)
    n = int(input())
    if n == 0:
        break

# 6072
n = int(input())
while 1 <= n <= 100:
    print(n)
    n -= 1

# 6073
n = int(input())
while 1 <= n <= 100:
    n -= 1
    print(n)
    if n == 0:
        break

# 6074
c = ord(input())
t = ord('a')
while t<=c :
  print(chr(t), end=' ')
  t += 1

# 6075
c = int(input())
t = 0
while t<=c :
  print(t, end=' ')
  t += 1
