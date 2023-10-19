# 6051
num1, num2 = map(int, input().split())
if num1 != num2:
    print(True)
else:
    print(False) 

# 6052
num = int(input())
print(bool(num))

# 6053
a = bool(int(input()))
print(not a)

# 6054
num1, num2 = map(int, input().split())
if bool(num1) & bool(num2) == True:
    print(True)
else:
    print(False)

# 6055
num1, num2 = map(int, input().split())
if bool(num1) | bool(num2) == True:
    print(True)
else:
    print(False)