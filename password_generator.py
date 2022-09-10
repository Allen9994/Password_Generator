import random
print("WELCOME TO PASSWORD GENERATOR!\n")
flag = True

while(flag):
    m = input("Enter level of password difficulty\n(1 for alphanumeric & 2 for special characters)\n")
    if len(m) != 1:
        print("Try again")
    elif ord(m) >= 49 and ord(m) <= 50:
        flag = False
        m = int(m)
        
flag = True
if m == 1:
    li = [0,1,2,3,4]
else:
    li = [0,1,2,3,4,5]
    
while(flag):
    n = input("Enter length of the password \n(minimum : 8 & maximum : 20)\n")
    if n.strip().isdigit():
        if int(n)>=8 and int(n)<=20:
            flag = False
            n = int(n)

for x in range(n-len(li)):
    li.append(random.choice(li))
    
random.shuffle(li)
print("Your password is: ",end = '')

for i in range(n):
    if li[i] == 5:
        c = chr(random.randint(33,47))
        print(c,end = '')
    elif li[i] == 4:
        c = chr(random.randint(65,77))
        print(c,end = '')
    elif li[i] == 3:
        c = chr(random.randint(78,90))
        print(c,end = '')
    elif li[i] == 2:
        c = chr(random.randint(97,110))
        print(c,end = '')
    elif li[i] == 1:
        c = chr(random.randint(111,122))
        print(c,end = '')
    else:
        c = chr(random.randint(48,57))
        print(c,end = '')
