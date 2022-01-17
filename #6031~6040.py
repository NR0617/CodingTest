# 6031
a=int(input())
print(chr(a))
# 6032
n=int(input())
print(-n)
# 6033
print(chr(ord(input())+1))
c=chr(ord(input())+1)
print(c)
n1=input()
n2=ord(n1)+1
s=chr(n2)
print(s)
# 6034
a, b=input().split()
c=int(a)-int(b)
print(c)
# 6035
a, b= input().split()
c=float(a)*float(b)
print(c)
# 6036
s= input().split()
print(s[0] * int(s[1]))
a, b=input().split()
b=int(b)
print(a*b)
# 문자열 * 정수 또는 정수 * 문자열은 그 문자열을 여러 번 반복한 문자열을 만들어 준다.
# 입력-단어와 반복 횟수가 공백으로 구분되어 입력된다.
# 출력-입력된 단어를 입력된 횟수만큼 반복해 출력한다.
# 6037
a=int(input())
b=input()
print(a*b)
# 6038
a, b = input().split()
c = int(a)**int(b)
print(c)
# 6039
a, b=input().split()
f1=float(a)
f2=float(b)
print(f1**f2)
f1, f2 = input().split()
f3 = float(f1)**float(f2)
print(f3)
# 6040
a, b=input().split()
print(int(a)//int(b))
