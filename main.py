a1 = int(input())
s = a1
s2 = 0 + abs(a1 ** 2)
while s != 0:
    a1 = int(input())
    s = s + a1
    s2 = s2 + abs(a1) ** 2
    if s == 0:
        break
print(s2)
print('================================')
A = float(input())
B = float(input())
C = str(input())
if C == '+':
    print(A + B)
elif C == '-':
    print(A - B)
elif C == '*':
    print(A * B)
elif C == '/' and B == 0:
    print("Division by 0!")
elif C == '/' and B != 0:
    print(A / B)
elif C == 'mod' and B == 0:
    print('Division by 0!')
elif C == 'mod' and B != 0:
    print(A % B)
elif C == 'pow':
    print(A ** B)
elif C == 'div' and B == 0:
    print('Division by 0!')
elif C == 'div' and B != 0:
    print(A // B)

a = int(input())
b = []
for i in range(a):
    x = input().lower()
    if x not in b:
        b.append(x)
