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

def acceptprime(prime):
    number = input("Enter the " + prime + " number : ")
    n = checkint(number)
    m = checkprime(n)
    if m!=None:
        return m
    else:
        print("Invalid ",prime," number")
        return acceptprime(prime)

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

def acceptprimitive():
    while True:
        number = input("Enter the primitve root : ")
        n = checkint(number)
        return n

def acceptk(p):
    print("Enter the value of K : ",end="")
    number = input()
    k = checkint(number)
    if(1<k<p-2):
        return k
    else:
        print("Enter the value between valid range (1<k<p-2)")
        return acceptk(p)
    
def acceptag(p):
    print("Enter the value of a : ",end="")
    number = input()
    a = checkint(number)
    if(1<a<p):
        return a
    else:
        print("Enter the valid range of a (1<a<p)")
        return acceptag(p)   

def acceptplain(p):
    number = input("Enter the plain text here : ")
    pt = checkint(number)
    if (0<=pt<p):
        return pt
    else:
        print("Enter the valid range of plain text (0<pt<p)")
        return acceptplain(p) 

prime = acceptprime("prime")
#prime = checkprime(number)
# if prime==None:
#     print(number," is not prime number")
#     print("so can't go further")
#     print("So Accepting Another prime number")
#     #sys.exit(0)
#     number = accept("prime")
#     prime = checkprime(number)
    

number1 = acceptprimitive()
list2 = list()
list2 = primitive(prime,number1)
if list2==None:
    print(number1," is not primitive root of ",prime)
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
    

print("All the primitive roots of ",prime," is as follows ")
print(list4)
print("total number of primitive roots of ",prime," is ",len(list4))
        
print()
print("*******************Encryption********************")
print()
p = prime
print("The value of prime p is ",p)
g = list4[0]
print("the value of generator g is ",g)
# a = 3
# print("the value of secerate key is--> a : ",a)
a= acceptag(p)
A = (g**a)%p
print("the Calculated value of A is ", A)

k = acceptk(p)

c1 = (g**k)%p
# number4 = input("Enter the plain text number  :")
# pt = checkint(number4)

pt = acceptplain(p)
c2 = ((pt*(A**k))%p)


print("the value of c1 and c2 is ",c1," ",c2)
print()
print("************************Decryption************************")
print()
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
