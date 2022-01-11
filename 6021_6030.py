#6021
a=input()
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
#6022
b=input()
print(b[0:2], b[2:4], b[4:6], sep=' ')
c=input()
print(c[:2]+' '+c[2:4]+' '+c[4:])
a=input()
print(a[0:2])
print(a[2:4])
print(a[4:6])
#6023
t=input().split(':')
print(t[1])
h,m,s=input().split(':')
print(m)
#6024
a,b = input().split()
c=a+b
print(c)
a,b = input().split()
print(a+b)
#6025
a, b=input().split()
c=int(a)+int(b)
print(c)
a, b=input().split()
print(int(a)+int(b))
a, b = input().split()
a=int(a)
b=int(b)
c=a+b
print(c)
#6026
a =float(input())
b =float(input())
print(a+b)
a=input()
b=input()
a=float(a)
b=float(b)
c=a+b
print(c)
#6027
a=int(input())
print('%x'%a)
#6028
a=int(input())
print('%X'%a)
#6029
b=int(input(),16)
print('%o'%b)
#6030
print(ord(input()))
a=ord(input())
print(a)
