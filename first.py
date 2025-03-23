import sys
def checkint(number):
    while True:
        if number.isdigit()==True:
            n = int(number)
            return n
        else:
            print("Invalid Input")
            number = input("Enter the correct Number : ")


def checkprime(number):
    count = 0
    for i in range(1,number+1):
        if number%i==0:
            count = count + 1

    if count==2:
        return number
    else:
        return None

def accept(prime):
    number = input("Enter the " + prime + " number : ")
    n = checkint(number)
    return n

def primitive(prime,root):
    list1 = list()
    for i in range(1,prime):
        k = (root**i)%prime
        if k in list1:
            return None
        else:
            list1.append(k)
    return list1


def findprimitive(prime,root):
    list3 = []
    for i in range(1,prime):
        s = (root**i)%prime
        if s in list3:
            return None
        else:
            list3.append(s)
    return root
        
number = accept("prime")
prime = checkprime(number)
if prime==None:
    print(number," is not prime number")
    print("so can't go further")
    print("So Accepting Another prime number")
    #sys.exit(0)
    number = accept("prime")
    

number1 = accept("primitive root")
list2 = list()
list2 = primitive(prime,number1)
#list2.sort()
print("printing the primitve value by the root of ", number1)
print(list2)

list4 = list()
for j in range(1,prime):
    pr = findprimitive(prime,j)
    if pr==None:
        pass
    else:
        list4.append(pr)
    

print("All the primitive roots list as follows")
print(list4)
print("total number of primitive roots of ",prime," is ",len(list4))
        

p = prime
print("The value of prime p is ",p)
g = list4[0]
print("the value of generator g is ",g)
a = 3
print("the value of secerate key is--> a : ",a)
A = (g**a)%p
print("the value of A is ", A)
number3 = input("Enter the ephemeral key k : ")
k = checkint(number3)
c1 = (g**k)%p
number4 = input("Enter the plain text number  :")
pt = checkint(number4)
c2 = ((pt*(A**k))%p)


print("the value of c1 and c2 is ",c1," ",c2)

print("Cipher to plain text is given below as ")
inv=0
print("the vlue of c1^a is ", c1**a%p)
for i in range(1,p):
    k = i*(c1**a)%p
    if k==1:
        inv = i
        break
print("the value of inverse is ", inv)
pt1 = ((c2*inv)%p)
print("The original plain text is here ", pt1)
