# 6084
print(round(h*b*c*s/8/1024/1024, 1), "MB")
h, b, c, s = map(int, input().split())
mb = round((h * b * c * s / 8) / 1024 / 1024, 1)
print('{} MB'.format(mb))
h, b, c, s = map(int, input().split())
mb = (h * b * c * s / 8) / 1024 / 1024
print('%.1f MB'%mb)
# 6085
w, h, b = map(int, input().split())
s = w*h*b/8/1024/1024
print('%.2f MB'%s)
w,h,b = input().split()
res=int(w)*int(h)*int(b)/1024/1024/8
print('%.2f'%res,"MB")
w, h, b = map(int, input().split())
mb = round(((w*h*b) / 8 / 1024 / 1024), 2)
print('{:.2f} MB'.format(mb))
# 6086
n = int(input())
s = 0
for i in range(1, n + 1):
    s += i
    if s>=n :
        break
print(s)
a=int(input())
s=0
c=0
while True:
    s=s+c
    c=c+1
    if s>=a:
        break
print(s)
