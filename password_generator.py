import random
i = 0
print("WELCOME TO PASSWORD GENERATOR!\n")
while(i == 0):
    m = input("Enter level of password difficulty\n(1 for alphanumeric 2 for special characters)\n")
    if len(m) == 0:
        print("Try again")
    elif ord(m) >= 49 and ord(m) <= 50:
        i = 1
i = 0
m = int(m)
if m == 1:
    li = [0,1,2]
else:
    li = [0,1,2,3]
while(i == 0):
    n = input("Enter length of the password (minimum : 8 maximum : 20)")
    if len(n) == 0:
        print("Try again")
    elif int(n)>=8 and int(n)<=20:
        i = 1
n = int(n)
for x in range(n-len(li)):
    li.append(random.choice(li))
random.shuffle(li)
print("Your password is: ",end = '')
for i in range(n):
    f = li[i]
    if f == 3:
        c = chr(random.randint(33,47))
        print(c,end = '')
    elif f == 2:
        c = chr(random.randint(65,90))
        print(c,end = '')
    elif f == 1:
        c = chr(random.randint(97,122))
        print(c,end = '')
    else:
        c = chr(random.randint(48,57))
        print(c,end = '')
    
