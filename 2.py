#6011
f=input()
f=float(f)
print(f)
print(float(input()))
#6012
a=int(input())
b=int(input())
print(a)
print(b)
#6013
print('{1}\n{0}'.format(input(),input()))
a=input()
b=input()
print('{1}\n{0}'.format(a,b))
#6014
a=float(input())
print(a)
print(a)
print(a)
a=float(input())
for i in range(3):
    print(a)
#6015
a, b=input().split()
print(a)
print(b)
a, b=input().split()
print('{}\n{}'.format(int(a),int(b)))
a, b=input().split()
print('{0}\n{1}'.format(a, b))
#6016
a, b=input().split()
print('{} {}'.format(b,a))
a, b=input().split()
print(b)
print(a)
#6017
a=input()
print(a,a,a)
#6018
a, b = input().split(':')
print(a, b, sep=':')
#6019
a=input().split('.')
a.reverse()
print('-'.join(a))
a,b,c=input().split('.')
print(c,b,a,sep='-')
#6020
a=input().split('-')
print(''.join(a))
a, b = input().split('-')
print(a,b,sep='')