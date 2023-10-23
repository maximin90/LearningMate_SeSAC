# 6061
x,y = map(int, input().split())
print(x|y)

# 6062
x,y = map(int, input().split())
print(x^y)

# 6063
a,b= map(int, input().split())
print(a if (a>=b) else b)

# 6064
a,b,c= map(int, input().split())
print((a if (a<b) else b) if ((a if a<b else b)<c) else c)

# 6065
a,b,c= map(int, input().split())
if a % 2==0:
    print(a)
if b % 2 == 0:
    print(b)
if c % 2 == 0:
    print(c)