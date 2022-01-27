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
