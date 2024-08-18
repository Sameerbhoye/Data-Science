# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 08:30:19 2024

@author: samir
"""
############################################################
'''Session 2    15/03/2024'''
print("Hello world")
x=True
y=False
print(x+x)

##############################################################
'''Session 3    19/03/2024'''
###############################################################################

a=None #NoneType
print(type(a))
print(a is None) #is operator
print(a is not None) #is not operator

############################################################

num=int(input("Enter number to check whether it is positive or negative :"))
if(num<0):
    print("Number is negative ")
elif(num>0):
    print("Number is Positive ")
else:
    print("Number is 0 ")
    
#############################################################

savings=float(input("Enter Your Savings :"))
if(savings==0):
    print("Sorry no Savings !!")
elif(savings<500):
    print("Well done")
elif(savings<1000):
    print("Thats a tidy sum")
elif(savings<10000):
    print("Welcome Sir")
else:
    print("Thank You")

#################################################

count=0
print('starting')
while(count!=11):
    print(count)
    count+=1

######################################################

'''Session 4   20/03/2024'''

#odd numbers

start, end= 4,19
for num in range(start, end+1):
    if(num%2!=0):
        print(num , end=" ")
    
#####################################################

#even numbers
start, end= 4,19
for num in range(start, end+1):
    if(num%2==0):
        print(num , end=" ")

#####################################################

#dictionary
s={"name":"Samar","age":22}
print(type(s))
print(s["name"])
for i in s:
    print(s[i], end= " ")
print()
print(len(s))
print(s.keys())
print(s.values())

######################################################

#string

x="I am Batman.I am vengeance."
print(x[:12])
print(x[12:])
print(x[::-1])
print(x[::-2])
print(x[-5:-1])

#palindrome
x=input("Enter name: ")
if(x==x[::-1]):
    print("string is Palindrome")
else:
    print("string is not palindrome")

####################################################

#strip function

x="   I am Batman . i am vengeance."
print(x.strip())

#replace 
print(type(x.replace("Batman","Spiderman").strip().split(' ')))

##################################################################

print(x.find("and"))
#checks whether the subtring is present in the main string or not 


x="I am Batman."
y="I am vengeance."
print(x+" "+y)

#######################################################

x=21
print(f"I am Samar and I am {x} years old")

#######################################################

# use of fstring / formated string
quantity=3
item_num=634
price=69
print(f"I want {quantity} pieces. Item number is {item_num}. Price is {price}")

##########################################################

''' Format Method '''
my_order="I want {} pieces. Item number is {}. Price is {}"
print(my_order.format(quantity,item_num,price))

my_order="I want {2} pieces. Item number is {0}. Price is {1}"
print(my_order.format(item_num,price,quantity))

###########################################################

#Escape character
print("My name is \"Samar\"") #with esacape character
#print ("My name is Samar"") #without escape character

print(3**(3-2)/3*4+6)

################################################################

'''Lists
   Properties
   1.mutable
   2.allows duplicate values 
   3.allows mixed data type'''
   
lst="cherry banana apple peach".split(' ')
print(lst)
lst.append("orange")
print(lst)
lst.extend("strawberry blueberry raspberry" .split())
print(lst)

#pop()
lst.pop(3)
print(lst)

#count()
print(lst.count("mango"))

#remove()
lst.remove("cherry")
lst.remove(3)
print(lst)

#sort()
lst.sort()
print(lst)

lst1=["red","blue","green"]

########################################################
'''Tuple
   Properties
   1.immutable
   2.allows mixed datatype'''
tup=("apple","cherry","banana")
y=list(tup)
y[1]="kiwi"
x=tuple(y)
print(x)
z=tup+x
print(z)

######################################################

'''Dictionaries'''

dict={"brand":["Maruti","Mahindra","Toyota"],"model":["a","b","c"],"year":[2021,2022,2023]}
print(dict)
print(dict.keys())
print(dict.values())
print(dict.get("model"))
dict1={"brand":"Ford","model":"Mustang","year":2024}
print(dict1)
dict1["color"]="yellow"
print(dict1)
print(dict1.get("brand"))
print(dict1.items())
dict1
dict1.pop("year")
print(dict1)
for x in dict1.values():
    print(x)
for x in dict1:
    print(x)
for key, value in dict1.item():
    print("%s=%s"%(key,value))

#copy
dict2=dict1.copy()
print(dict2)

#Dictionary inside Dictionary

myFamily={"child1":{"Name":"Samar","age":21},"child2:":{"Name":"Shekhar","age":19}}
print(myFamily)
#myFamily.clear()
x={"abc","def","ghi"}
y=0
dict1=dict.fromkeys(x,y)
print(dict1)
print(dict1.get("abc"))
print(dict1.items())
print(dict1.keys())
print(dict1.values())
myFamily["child1"].update({"height":180})
print(myFamily)
#
myFamily.replace("child2","child3")
print(myFamily)
#AttributeError: 'dict' object has no attribute 'replace'

##########################################################

#control Flow statement
lst

#break
for i in lst:
    print(i)
    if(i=="banana"):
        break

#continue
for i in lst:
    #print(i)
    if(i=="banana"):
        continue
    print(i)
#continue will skip the banana and keep iterating

####################################################

#Range Function

for x in range(2,30,3):
    print(x)

for x in lst1:
    for y in lst:
        print(x,y)
        
#Functions 

def add(a,b):
    c=a+b
    print("addition=",c)
add(6,5)

############################################################################

#arbitary arguments  (*args)

def myFunc(*name):
    print(name[1]+" "+name[3])
myFunc("hello","hi","world","Samar")
    
#############################################################################

#kwargs / keyword arguments (**args)

def func1(**name):
    for key, value in name.items():
        print("%s= %s"%(key,value))
func1(first="Sameer", mid="Ashok",last="Bhoye")
   
#Functions with default arguments 

def func(country="India"):
    print("I am from "+country)
func("Norway") #if argument passed explicitly it is used 
func("Sweden")
func()         #if argument not passed explicitly default argument (here  India)  is used

def func1(lst):
    for i in lst:
        print (i)
func1(lst)

############################################################################################

#Function with return value 

def fun(x):
    return x*x
print(f"square of 5 is  {fun(5)}")

##########################################################################

#Pass Function 

def fun():
    #print("Hello World")
    pass
fun()

################################################################################

#Factorial of number
def factorial(x):
    if(x==1):
        return 1
    elif(x==0):
        return 1
    else:
        return (x*factorial(x-1))
print(f"Factorial of 0 is {factorial(5)}")

###############################################################################

#Lambda Function 

#can have multiple arguments but only one expression 

def add(a,b):
    return (a*b)/3
print(add(2,3))

#same as above 
add=lambda a,b: (a*b)/3
print(add(2,3))
     
################################################################################

odd_list=list(filter(lambda x:(x%2!=0),lst))
print(odd_list)

#square numbers 
lst=[1,2,3,4,5,6,7,8,9]
sqlst=[]
sqlst.extend(list(map (lambda x:x**2,lst)))
print(sqlst)

lst_sq=[]
for i in lst:
    lst_sq.append(i**2)
print(lst_sq)

a=lambda x:x*x
for x in lst:
    sqlst.append(a(x))
print(sqlst)

#############################################################################

print("Welcome to the Roller Coaster")
height=int(input(" Please Enter your height:"))
if(height>=120):
    bill=0
    print("You are elligible for Roller Coaster !")
    
    age=int(input("Please enter your age : "))
    if(age<=12):
        print("child ticket is $5")
        bill+=10
    elif(age>=18):
        print("your ticket is $10")
        bill+=15
    elif(age<=60):
        print("your ticket is $15")
        bill+=20
    else:
        print("As you are old you are not elligible !")
    print("Do You need Popcorn : ")
    p=int(input("Enter 1 for popcorn:"))
    if(p==1):
        print("Enjoy your popcorn ")
        bill+=5
        print(f"You need to pay {bill}")
    else:
        print(f"you need to pay {bill}")
    print("Do you need photo :")
    need_photo=(input("Enter y or n :"))
    if(need_photo=='y'):
        bill+=3
        print(f"you need to pay {bill}")
    else:
        print(f"you need to pay {bill}")
        
'''BMI CALCULATOR'''
height=float(input("Enter your height in m :"))
weight=float(input("Enter you weiht in kg :"))
BMI=round((weight/(height*height)),2)
if(BMI<18.5):
    print(f"You are under weight and BMI is {BMI}")
elif(BMI>18.5 and BMI<25):
    print(f"You are normal weight and BMI is {BMI}")
elif(BMI>25 and BMI <30):
    print(f"you are over weight and BMI is {BMI}")
elif(BMI>30 and BMI<35):
    print(f"you are obese and BMI is {BMI}")
else:
    print(f"you are clinically obese and BMI is {BMI}")
    
#duplicates in list
lst1=[1,2,3,4,5,7,5,3]
def dup_lst(lst1):
    for i in range(len(lst1)-1):
        if(lst1[i]==lst1[i+1]):
            return True
    return False
print(dup_lst(lst1))

lst1=[1,2,3,4,5,5]
lst1.sort()
lst1
def dup_lst(lst1):
    for i in range(len(lst1)-1):
        if(lst1[i]==lst1[i+1]):
            return True
    return False
print(dup_lst(lst1))

###########################################################################

def is_leapYear(year):
    if((year>0) & ((year%4==0) & (year%100!=0)) | ((year%400==0) & (year%100==0))):
        return True 
    return False 
if(is_leapYear(2024)):
    print("Leap year ")
else:
    print("Not a Leap Year ")

##########################################################################################

#mario pyramid

for i in range(4):
    for j in range(i+1):
        print("#", end=" ")
    print()

for i in range(6):
    for j in range(i-1):
        print("#", end=" ")
    print()

#def diamond():
    






#################################################################################

#min max element 
lst=[1,2,3,4,5,6,7,8,9]
def min_max(lst):
    min=lst[0]
    for i in lst:
        if(i<min):
            min=i
        max=lst[0]
        if(i>max):
            max=i
    print(f"min={min} and max={max}")
min_max(lst)

####################################################################################

str=input("Enter:")
if(str==str[::-1]):
    print("yes")
else:
    print("no")
users="admin employee manager worker staff".split(" ")
for users in users:
    users=input("Enter Role:")
    if(users=="admin"):
        print("Hello admin")
    elif(users=="employee"):
        print("Hello employee")
    elif(users=="manager"):
        print("Hello manager")
    elif(users=="worker"):
        print("Hello workers")
    else:
        print("Hello staff")
        
############################################################################################
  




















