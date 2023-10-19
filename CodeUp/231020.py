# 6056
num1, num2 = map(int, input().split())
if bool(num1) != bool(num2):
    print(True)
else:
    print(False)

# 6057
num1, num2 = map(int, input().split())
if bool(num1) == bool(num2):
    print(True)
else:
    print(False)

# 6058
num1, num2 = map(int, input().split())
if bool(num1) == bool(num2) == False:
    print(True)
else:
    print(False)
    
# 6059
a = int(input())
print(~a)

# 6060
num1, num2 = map(int, input().split())
result = num1 & num2 
print(result)