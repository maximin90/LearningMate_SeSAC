# 6076
n = int(input())
for i in range(n+1) :
  print(i)

# 6077
n = int(input())
sum = 0
for i in range(1, n+1):
    if i % 2 == 0:
        sum += i
print(sum)

# 6078
while True:
    x = input()
    print(x)
    if x == 'q':
        break

# 6079
n = int(input())
sum = 0
cnt = 0

while (sum < n):
    cnt += 1
    sum += cnt

print(cnt)

# 6080
n, m = map(int, input().split())

for i in range(1, n+1):
    for j in range(1, m+1):
        print(i, j)
