# 6041
a, b = map(int, input().split())
print(a % b)

# 6042
num = float(input())
print("%.2f" % num)

# 6043
f1, f2 = map(float, input().split())
print("%.3f" %(f1/f2))

# 6044
a, b = map(int, input().split())
print('%d \n%d \n%d \n%d \n%d \n%.2f' % (a+b,a-b,a*b, a//b, a%b, a/b))

# 6045
a,b,c = map(int, input().split())
r1 = a + b +c
r2 = (a+b+c) / 3
print('%d %.2f' % (r1, r2))