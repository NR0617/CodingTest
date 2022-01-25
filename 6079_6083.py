# 6079
a = int(input())
s = 0
i = 0
while s < a:
    i += 1 # t = t+1
    s += i # s = s+t
print(i)
# 6080
n, m = map(int, input().split())
for i in range(1, n+1):
    for j in range(1, m+1):
        print('{} {}'.format(i,j))
# 6081
n = input()
for i in range(1, 15 + 1):
	print('%x*%x=%x'.upper() %(int(n, 16), int(hex(i), 16), (int(n, 16) * int(hex(i), 16))))
n = int(input(), 16)
for i in range(1, 16) :
    print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='') # 또는 print("%X*%X=%X"%(n,i,n*i))
    #sep=''입력시 공백 없이 출력
# 6082
s = int(input())
for i in range(1, s+1):
    if i%10 == 3 or i%10 == 6 or i%10 == 9:
        print('X', end=" ")
    else:
        print(i, end=" ")
# 6083
a, b, c = map(int, input().split())
count = 0
for i in range(a):
    for j in range(b):
        for k in range(c):
            print('{} {} {}'.format(i, j, k))
            count += 1
print(count)
r, g, b = input().split()
r = int(r)
g = int(g)
b = int(b)
for i in range(0, r) :
  for j in range(0, g) :
    for k in range(0, b) :
      print(i, j, k)
print(r*g*b)
