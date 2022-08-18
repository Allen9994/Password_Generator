import random
i = 0
print("WELCOME TO PASSWORD GENERATOR!\n")
while(i == 0):
    m = int(input("Enter level of password difficulty\n(1 for alphanumeric 2 for special characters)\n"))
    if m >=1 and m <=2:
        i = 1
i = 0
m = m + 1
while(i == 0):
    n = int(input("Enter length of the password (minimum : 8 maximum : 20)"))
    if n>=8 and n<=20:
        i = 1
print("Your password is: ",end = '')
for i in range(n):
    f = random.randint(0,m)
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
    
