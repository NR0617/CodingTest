# 6056
a, b = input().split()
c = bool(int(a))
d = bool(int(b))
print((c and (not d))or((not c) and d))
a, b = map(int, input().split())
if (bool(a) != bool(b)):
    print(True)
else:
    print(False)
# 6057
a, b = input().split()
c = bool(int(a))
d = bool(int(b))
print((c and d) or ((not c)and(not d)))
print(a==b)
a, b = map(int, input().split())
if (bool(a) == bool(b)):
    print(True)
else:
    print(False)
# 6058
a, b = input().split()
c = bool(int(a))
d = bool(int(b))
print(c == d == False)
a, b = input().split()
c = bool(int(a))
d = bool(int(b))
print(not (c or d))
a, b = map(int, input().split())
print(bool(a) is False and bool(b) is False)
# 6059
a = int(input())
print(~a)
# 6060
a, b = map(int, input().split())
c = a&b
print(c)
# 6061
a, b = map(int, input().split())
print(int(a|b))
a, b = input().split()
print(int(a) | int(b))
# 6062
a, b = input().split()
print(int(a)^int(b))
# 6063
a, b = input().split()
a = int(a)
b = int(b)
c = a if(a>=b) else b
print(c)
a, b = map(int, input().split())
print(a if a>b else b)
# 6064
a, b, c = map(int, input().split())
d = (a if a<b else b) if(a if a<b else b)<c else c
print(d)

a, b, c = input().split()
a = int(a)  #변수 a에 저장되어있는 값을 정수로 바꾸어 다시 변수 a에 저장
b = int(b)
c = int(c)
d = a if a<b else b
e = d if d<c else c
print(e)
# 6065
a, b, c = map(int, input().split())
if a%2==0:
    print(a)
if b%2==0:
    print(b)
if c%2==0:
    print(c)
