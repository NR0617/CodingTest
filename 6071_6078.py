# 6071
i = True
while(i):
    num = int(input())
    if(num == 0):
        i = False
    else:
        print(num)
while True:
    a=input()
    a=int(a)
    if a==0:
        break
    else:
        print(a)
# 6072
i = int(input())
while i!=0:
    print(i)
    i=i-1
num = int(input())
while(num > 0):
    print(num)
    num -= 1
# 6073
num = int(input())
while num > 0:
    num -= 1
    print(num)
# 6074
t = ord(input())
a = ord('a')
while a <= t:
    print(chr(a), end=' ')
    a += 1
a = input()
count = 0
while(count <= ord(a)-97):
    print(chr(97+count), end=' ')
    count += 1
# 6075
num = int(input())
i = 0
while i <= num:
    print(i)
    i += 1
n = int(input())
for i in range(n + 1):
    print(i)
# 6076
n = int(input())
for i in range(n + 1):
    print(i)
# 6077
n = int(input())
s = 0
for i in range(1, n+1):
    if i%2 == 0:
        s += i
print(s)
# 6078
c = ''
while c != 'q':
    c = input()
    print(c)
while True:
    k = input()
    print(k)
    if k == 'q':
        break
