# 6087
num = int(input())
for i in range(1, num+1):
    if i % 3 != 0: 
        print(i)
        i += 1
n=int(input())
for i in range(1, n+1) : 
    if i%3==0 : 
        continue            #다음 반복 단계로 넘어간다.
    print(i, end=' ')    #i가 짝수가 아닐 때만 실행된다.
n = int(input())
for i in range(1, n + 1):
    if(i % 3 == 0):
        pass
    else:
        print(i)
# 6088
a, d, n = map(int, input().split())
for i in range(2, n+1):
    a = a + d
print(a)
a, b, n = map(int, input().split())
total = a
for i in range(a, a + n - 1):
	total += b
print(total)
a,d,n=input().split()
a=int(a)
d=int(d)
n=int(n)
s=a
for i in range(2, n+1):
    s+=d
print(s)
# 6089
a, r, n = map(int, input().split())
result = a
for i in range(2, n+1):
    result = result * r
print(result)
a, b, n = map(int, input().split())
total = a
for i in range(a, a + n - 1):
	total *= b
print(total)
a, r, n = input().split()
a = int(a)
r = int(r)
n = int(n)
for i in range(1, n) :
    a = a*r
print(a)
# 6090
a, m, d, n = map(int, input().split())
for i in range(1, n):
    a = a*m + d
print(a)
a, m, d, n = map(int, input().split())
total = a
for i in range(a, a + n - 1):
	total = total * m + d
print(total)
