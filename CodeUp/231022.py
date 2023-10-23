# 6066
a, b, c = map(int, input().split())

for i in a,b,c:
    if i % 2 == 0:
        print('even')
    else:
        print('odd')

# 6067
x = int(input())
if x < 0 and x % 2 == 0:
    print('A')
elif x < 0 and x % 2 == 1:
    print('B')
elif x > 0 and x % 2 == 0:
    print('C')
elif x > 0 and x % 2 == 1:
    print('D')

# 6068
score = int(input())
if 90 <= score <= 100:
    print('A')
elif 70 <= score <= 89:
    print('B')
elif 40 <= score <= 69:
    print('C')
elif 0 <= score <= 39:
    print('D')

# 6069 -> 리스트 사용해서 만들어보고 시품 🐱‍💻
msg = input()
if msg == 'A':
    print('best!!!')
elif msg == 'B':
    print('good!!')
elif msg == 'C':
    print('run!')
elif msg == 'D':
    print('slowly~')
else:
    print('what?')

# 6070
month = int(input())
if month // 3 == 1:
    print('spring')
elif month // 3 == 2:
    print('summer')
elif month // 3 == 3:
    print('fall')
else:
    print('winter')