# 6066
a, b, c = map(int, input().split())
if a%2 == 0:
    print('even')
else:
    print('odd')
if b%2 == 0:
    print('even')
else:
    print('odd')
if c%2 == 0:
    print('even')
else:
    print('odd')
data = input().split()
for i in data:
    if(int(i) % 2 == 0):
        print('even')
    else:
        print('odd')
# 6067
num = int(input())
# if num != 0:
if num < 0:
    if num % 2 == 0:
        print('A')
    else:
        print('B')
else:
    if (num % 2 == 0):
        print('C')
    else:
        print('D')
        data = int(input())
if(data % 2 == 0 and data < 0):
    print('A')
elif(data % 2 != 0 and data < 0):
    print('B')
elif(data % 2 == 0 and data > 0):
    print('C')
elif(data % 2 != 0 and data > 0):
    print('D')
# 6068
score = int(input())
if score >= 90:
    print('A')
else:
    if score >= 70:
        print('B')
    else:
        if score >= 40:
            print('C')
        else:
            print('D')
score = int(input())
if(score >= 90):
    print('A')
elif(score >= 70):
    print('B')
elif(score >= 40):
    print('C')
elif(score >= 0):
    print('D')
# 6069
score = input()
if score == "A":
    print("best!!!")
elif score == "B":
    print("good!!")
elif score == "C":
    print("run!")
elif score == "D":
    print("slowly~")
else:
    print("what?")
# 6070
mth = int(input())
if mth//3 == 1:
    print('spring')
elif mth//3 == 2:
    print('summer')
elif mth//3 == 3:
    print('fall')
else:
    print('winter')
