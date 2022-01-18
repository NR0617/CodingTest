# 6041
a,b =input().split()
c=int(a)//int(b)
print(c)
# 6042
a=float(input())
print(format(a, ".2f"))
f = float(input())
print(round(f,2))
print(round(float(input()), 2))
# 6043
a, b=input().split()
c=round(float(a)/float(b),3)
print('%.3f'%c)
a,b=input().split()
a=float(a)
b=float(b)
c=a/b
print(format(c,".3f"))
a, b = map(float, input().split())
print('%.3f' %round((a / b), 3))
# 6044
a, b=input().split()
a=int(a)
b=int(b)
if(a>=0 and b!=0):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a//b)
    print(a%b)
    print(round((a/b),2))
# 6045
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
d = round(((a+b+c)/3),2)
print((a+b+c),'%.2f'%d)
a, b, c = input().split()
a=int(a)
b=int(b)
c=int(c)
hap=a+b+c
avg=hap/3
print(hap, format(avg, ".2f"))
