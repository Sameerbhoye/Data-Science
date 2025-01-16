###############BASIC OF PYTHON##################
#String Concat
a1=input("Enter a1 : ")
a2=input("Enter a2 : ")
print(a1+a2)

a1=int(input())
a2=int(input())
print(a1+a2)

#Complex
b1=1
b2=4j
print('b1 : ',b1,'  b2 : ',b2)
print(type(b1))
print(type(b2))
print(b1.real)
print(b2.imag)

#Bool
a=True
b=True
c=False
print(type(a))
print(a+b)
print(a-b)
print(a+c)
print(a-c)
print(c-a)
b=bool(input("Okee!!!! : "))
print(b)
print(type(b))

h=10
a=15
print(h+a)
print(type(h+a))
print(10*4)
print(type(10*4))
g1=10
g2=7
print(g1-g2)
print(type(g1-g2))
print(100/20)

#Mathematical Operators
print(100/2.7)
print(100//2.7)
print(100%13)
print(5**2)
x=1
x+=1
print(x)
x-=1
print(x)
x*=10
print(x)

#None Type
w=None
print(w is None)
print(w is not None)
print(type(w))

#IF Else Statements With Comparative Operators
a=int(input("Enter Any Number : "))
if a>0:
    print(a," Is Positive Number!!")
elif a==0:
    print(a," Is Zero!!")
elif a<0:
    print(a," Is Negative Number!!")
else:
    print("Invalid Input!!")

#While Loop
c=1
print("Start")
while c<=10:
    print(c)
    c+=1

#For Loop
print("Start")
for i in range(11):
    print(i)
for i in range(2,10):
    print(i)

a=int(input("Enter The Number To Run Loop Till It : "))
for i in range(0,20):
    if i==a:
        break
    print(i)
print("Done")

for _ in range(0,10):
    print("_",end=" ")
    print()

#Odd Numbers
s,e=4,19
for i in range(s,e+1):
    if i%2!=0:
        print(i,end=" ")

#Even Numbers
for i in range(0,21):
    if i%2==0:
        print(i,end=" ")
    
#Global Variable
x=25
def fun1():
    print(x)
fun1()

#Local Variable
x=10
def fun2():
    x=20
    print(x)
fun2()
print(x)

#Getting Datatypes
a={"Name":"Ram","Age":18}
b=(1,2,3,4)
c=['Ram',34,'Sham',22]
d={1,2,3,4}
#arr[5]={1,2,6,3,4,5}
print(type(a))
print(type(b))
print(type(c))
print(type(d))

#Cant Concat String With Integer
s1="Hello"
s2=2
print(s1+s2)

#Multiline String
x="""This Is First Line 
This Is Second Line"""
print(x)

#String Slicing
a="""This Is Python And I Am In Spyder"""
print(a[2:17])
print(a[3])
print(a[0:30:2])
#Slice From Start
print(a[:5])
#Slice From End
print(a[16:])
#Prints All
print(a[::])
#Negative Indexing
print(a[-3])
print(a[-5:-1])
#Reverse String
print(a[::-1])
print(a.upper())
print(a.lower())
print(a[::])
print(a.find('I'))

#Remove White Space
x="   This Is Python"
print(x)
print(x.strip())

#Replace Words
x="Hey This Is Python"
print(x)
print(x.replace("Hey","Hii"))

a="Hello World"
print(a.split())
print(a.split(" "))
x="Hello"
y="World"
print(x+y)
print(x+" "+y)

#F String Operator
x=18
print("Hii My Name Is Shekhar And My Age Is : ",x)
print(f"Hii My Name Is Shekhar And My Age Is : {x}")

q=3
n=54
p=67
print(f"I Want {q} Pieces Its Item Number Is {n} And Its Price Is {p}")

q=3
n=54
p=67
mo=("I Want {} Pieces Its Item Number Is {} And Its Price Is {}")
print(mo.format(q,n,p))

#With Indentation(IDs) 
q=3
n=54
p=67
mo=("I Want {0} Pieces Its Item Number Is {1} And Its Price Is {2}")
print(mo.format(q,n,p))

#To Print "" In String
print("Hey I Am Coding In \"Spyder\"")

#PEMDAS
print(3*3+3/3-3)

#List
l=["Handsome",19,5.6]
print(l)
print(l[1])
l.append("ECE")
print(l)
l.pop()
print(l)
#l.clear()
#print(l)
l2=l.copy()
print(l2)

l3=[2,4,6,8,2,14,6]
print(l3)
print(l3.count(2))
print(l3.count(8))
l4=[1,3,5,7,3,9,5]
print(l4)
l3.extend(l4)
print(l3)

l5=[1,2,3,4,5,6,7,8,9,10]
l5.insert(0,0)
l5.insert(2,15)
print(l5)
l5.pop()
print(l5)
l5.pop(2)
print(l5)
l5.remove(5)
print(l5)
print(len(l5))
l5.reverse()
print(l5)
l5.sort()
print(l5)

#Tuple
t=("Cherry","Cherry","Banana")
print(t)
print(t[2])
x=list(t)
x[1]="Kiwi"
t=tuple(x)
print(t)
tup=("Handsome",18,5.6)
print(tup)
tup1=t+tup
print(tup1)

#Dictionary
d={"Name":"Shekhar","Roll No":23,"Class":"SY A"}
print(d)
print(len(d))
print(d.get("Name"))

car={"Brand":["Maruti","Mahindra","Toyata"],
     "Model":["Alto","XUV 700","Fortuner"],
     "Year":[2010,2020,2018]}
print(car)

car={"Brand":"Ford","Model":"Mustang","Year":2024}
print(car)
print(car.keys())
print(car.values())
car["Color"]="Black"
print(car)
car.pop("Color")
print(car)
for x in car:
    print(car[x])
for key,value in car.items():
    print("%s = %s"%(key,value)) #Format Specifier
car2=car.copy()
print(car2)
car3=dict(car)
print(car3)
family={"Chlid1":{"Name":"Sham","DOB":"21-05-2009"},
        "Child2":{"Name":"Ram","DOB":"07-11-2007"}}
print(family)
car3.clear()
print(car3)

x={'key1','key2','key3'}
y=0
xy=dict.fromkeys(x,y)
print(xy)
print(car.items())
print(car)
car.update({"Color":"Black"})
print(car)

#Break And Continue
l=["Apple","Banana","Orrange","Mango"]
print(l)
for i in l:
    print(i)
    if i=="Banana":
        break
for j in l:
    if j=="Banana":
        continue
    print(j)

#For Loop Range
for i in range(0,31,3):
    print(i)
   
#Nested For Loop
colors=["Green","Yellow","Red"]
fruits=["Guava","Banana","Apple"]
for i in colors:
    for j in fruits:
        print(i,j)

#Functions
def func1():
    print("This Is Function")
func1()

def name(n):
    print("Your Name Is : "+n)
name("Shekhar")

#Functions With Positional Arguments
def full_name(first_name,surname):
    print("Your Full Name Is : "+first_name+" "+surname)
full_name("Shekhar","Autade")

#Arbitrary Arguments
def func(*kids):
    print(kids[0]+" "+kids[2])
func("Hello","World","India")

#Kwargs
def fun(**kwargs):
    for x,y in kwargs.items():
        print("%s=%s"%(x,y))
fun(Name="Shekhar",Class="SY",Rollno=23)

#Default Argument
def func(country="Norway"):
    print("I Am From : "+country)
func("Sweden")
func()
func("India")

#List In Argument
fruit=["Mango","Apple","Orange"]
def fun(fruit):
    for i in fruit:
        print(i,end=" ")
fun(fruit)

def mul5(x):
    return x*5 
mul5(5)

#Pass Function
def func():
    pass

#Recursive Function For Factorial
def factorial(x):
    if x==1:
        return 1  
    else:
        return(x*factorial(x-1))
factorial(3)
factorial(6)

#Lambda Function
add=lambda a:a*a
print(add(5))

add=lambda a,b:a+b
print(add(20,30))

lst=[34,12,64,55,75,13,63]
odd_lst=list(filter(lambda x:(x%2!=0),lst))
print(odd_lst)
even_lst=list(filter(lambda x:(x%2==0),lst))
print(even_lst)

lst=[3,5,6,1,4,7,8,9,10,2]
sqlst=list(filter(lambda x:x*x,lst))
print(sqlst)

'''
Write python code using logical operators and if elif.
so as to check height as weel as
so as to allow for roller coater also ask user age 
and charge ticket accordingly'''


print("Welcome to the roller coaster")
height=int(input("Please enter your height :"))
if height>=120:
    bill=0
    print("You are eligible for roller coaster !")
    
    
    age=int(input("Eneter your age in years :"))
  
    if age<=12:
        print("childs ticket is $5")
        bill+=10
    elif age>=18:
        print("Your ticket is $7")
        bill+=15
    elif age<=60:
        print("Your ticket is $10")
        bill+=20 
    else:
        print("As you are old you are not eligible ! ")
        
    print("Do you need popcorn ?")
    p=int(input("Enter 1 for popcorn :"))
    if p==1 :
        print("Enjoy your Popcorns ")
        bill+=5
        print(f"You need to pay {bill} ")
    else:
        print(f"You need to pay {bill}")
    print("Do you need photo ")
    Need_photo=(input("Enter Y or N :"))
    if Need_photo=='Y':
        bill+=3
        print(f"You need to pay {bill}")
    else:
        print(f"You you need to pay {bill}")
        
        
#BMI calculator
Height=float(input("Enter your height in m :"))
Weight=float(input("Enter your weight in kg :"))
BMI=round((Weight/(Height*Height)),2)
if BMI <18.5:
    print(f"You are under weight and your BMI is{BMI} !")
elif BMI>18.5 and BMI<25 :
    print(f"you are normal weight and your BMI is {BMI} !")
elif BMI>25 and BMI<30:
    print(f"You are over weight and your BMI is {BMI} !")
elif BMI>30 and BMI<35:
    print(f"You are obese and your BMI is {BMI} !")
elif BMI>35:
    print(f"You are clinically obese and your BMI is {BMI} !")

#duplicates in list
lst1=[1,2,3,4,5,7,5,3]
def dup_lst(lst1):
    for i in range(len(lst1)-1):
        if(lst1[i]==lst1[i+1]):
            return True
    return False
print(dup_lst(lst1))

lst1=[9,2,7,4,1,5]
lst1.sort()
lst1

def leap_year(year):
    if((year>0) and (year%4==0) and (year%100!=0) or (year%400==0)):
        print("It Is Leap Year!!!")
    else:
        print("It Is Not Leap Year")
leap_year(2024)

#Pattern(Mario Pyramid)
for i in range(4):
    for j in range(4):
        print("*",end=" ")
    print()
    
for i in range(4):
    for j in range(i+1):
        print("*",end=" ")
    print()

for i in range(4):
    for j in range(4-i):
        print("*",end=" ")
    print()
    #print()
    
# Upper half of the diamond
for i in range(1, 6):
    print(" " * (5 - i) + "* " * i)

# Lower half of the diamond
for i in range(4, 0, -1):
    print(" " * (5 - i) + "* " * i)


lst=[23,45,2,1,5,7,8,12]
def min_max(lst):
    min=lst[0]
    for i in lst:
        if i<min:
            min=i
    print("Minimum Value Is : ",min)
    
    max=lst[0]
    for i in lst:
        if i>max:
            max=i
    print("Maximum Value Is : ",max)
print(min_max(lst))

def palindrome(word):
    a=word[::-1]
    if(a==word):
        print("String Is Palindrome")
    else:
        print("String Is Not Palindrome")
palindrome("step on no pets")

#users=["admin","employee","manager","worker","staf"]
i=input("Enter Your Post(in small letters) : ")
#for i in users:
if i=="admin":
    print("Hello Admin!!!")
elif i=="ceo":
    print("Hello CEO OF Company!!!")
elif i=="employee":
    print("Hello Employee !!!")
elif i=="manager":
    print("Hello Manager !!!")
elif i=="worker":
    print("Hello Worker !!!")
elif i=="staf":
    print("Hello Staff !!!")
else:
    print("Sorry No Post Available🥲")
    
lst=[]
for num in range(0,20):
    lst.append(num)
print(lst)

#########Comprehension#########
#List Comprehension
lst=[num for num in range(0,20)]
print(lst)   

names=["mama","dada","kaka"]
lst=[name.capitalize() for name in names]
print(lst)

#List Comprehension With If Statement 
def is_even(num):
    return num%2==0
lst=[num for num in range(10) if is_even(num)]
print(lst)

def is_odd(num):
    return num%2!=0
lst=[num for num in range(10) if is_odd(num)]
print(lst)

lst=[f"{x}{y}"for x in range(3) for y in range(3)]
print(lst)

#Dictionary Comprehension
dict={x:x*x for x in range(3)}
print(dict)

#Generators
gen=(x for x in range(3))
print(gen)
for num in gen:
    print(num)

gen=(x for x in range(3))
next(gen)
next(gen)

#Function Returning Multiple Values
def range_even(end):
    for num in range(0,end,2):
        yield num    #yield to return multiple values
for num in range_even(5):
    print(num)
gen=range_even(5)
next(gen)
next(gen)

#Chaining Generators
def lengths(itr):
    for ele in itr:
        yield len(ele)
def hide(itr):
    for ele in +itr:
        yield ele*'*'
'''
"ele*" appears to be a placeholder for an element from an iterable.The
asterisk(*) is likely just a character used to represent a placeholder
or a wildcard.
For instance,if you're iterating over a list of elements,"ele"
could symbolize any element in that list.
Its a generic representation that doesn't correspond to any specific
syntax in Python or iteratools
'''
passwords=["not-good","give m-pass"]
for password in hide(lengths(passwords)):
    print(password)

#Taking Password From User And Hiding
def lengths(password):
    for i in password:
        yield len(i)
def hide(password):
    for i in password:
        yield i*'*'
a=input("Enter The Password : ")
print("The Password Is Hidden : ")
for x in hide(lengths(a)):
    print(x,end="")

#Enumerates
lst=["Milk","Egg","Bread"]
for i in range (len(lst)):
    print(f"{i+1} {lst[i]}")
    
lst=["Milk","Egg","Bread"]
for i,item in enumerate(lst,start=1):
    print(i,"",item)

#Zip Function
lst1=["Sameer","Ashok","Bhoye"]
lst2=[101,102,103]
for l1,l2 in zip(lst1,lst2):
    print(l1,l2)

lst1=["Sameer","Ashok","Bhoye","Dada"]
lst2=[101,102,103]
from itertools import zip_longest
for l1,l2 in zip_longest(lst1,lst2):
    print(l1,l2)

lst1=["Sameer","Ashok","Bhoye","Dada"]
lst2=[101,102,103]
from itertools import zip_longest
for l1,l2 in zip_longest(lst1,lst2,fillvalue=0):
    print(l1,l2)

lst=[2,3,-6,0,9]
if all(lst):
    print("All Values Are True")
else:
    print("There Are Non Zero Values")

lst=[0,0,0,-8,0]
if any(lst):
    print("It Has Some Non Zero Values")
else:
    print("Useless")

lst=[0,0,0,0,0]
if any(lst):
    print("It Has Some Non Zero Values")
else:
    print("All Values Are Zero")
 
#Count Function From Itertools
from itertools import count
counter=count()
print(next(counter))
print(next(counter))
print(next(counter))
 
from itertools import count
counter=count(start=1)
print(next(counter))
print(next(counter))
print(next(counter))
   
#Cycle
import itertools
ins=("Eat","Code","Sleep")
for ints in itertools.cycle(ins):
    print(ints)

#Repeat
from itertools import repeat
for msg in repeat("Keep Patiance",times=3):
    print(msg)

#Combinations
from itertools import combinations
players=["Sammer","Ganesh","Shekhar"]
for i in combinations(players,2):
    print(i)
 
#Permutations
from itertools import permutations
players=["Sammer","Ganesh","Shekhar"]
for i in permutations(players,2):
    print(i)

#Product
from itertools import product
team_1=["Sammer","Ganesh","Shekhar"]
team_2=["Rehan","Bunty","Virendra"]
for i in product(team_1,team_2):
    print(i)

'''
In Python,assignment statement (obj_b = obj_a)
do not create real copies
It only creates a new variable eith the same reference.
So when you want to make actual copies of mutable object
(lists,dicts)
and want to modify the copy without affecting the original,
you have to be careful.
For 'real' copies we can use the copy module,
However,for compound/nested objects and custom objects there is an 
important difference between shallow and deep copy
'''
#Shallow Copy And Deep Copy
#Assignment operation
#This will only create a new variable with same reference.
list_1=[1,2,3,4,5]
list_2=list_1
list_1[0]=10
print(list_1)
print(list_2)

import copy
list_1=[1,2,3,4,5]
list_2=copy.copy(list_1)
print(list_1)
print(list_2)
list_2[0]=-10
print(list_1)
print(list_2)

#2-level deep
import copy
list_1=[[1,2,3,4,5],[6,7,8,9,10]]
list_2=copy.copy(list_1)
list_2[0][0]=-10
print(list_1)
print(list_2)

#Deep copy
import copy
list_1=[[1,2,3,4,5],[6,7,8,9,10]]
list_2=copy.deepcopy(list_1)
list_2[0][0]=-10
print(list_1)
print(list_2)

import pandas as pd
f1=pd.read_csv('buzzers.csv')
print(f1)

#import os
with open('buzzers.csv') as raw_data:
    print(raw_data.read())


###############################################################################
#read csv data in the form of list

import csv
with open('buzzers.csv') as raw_data:
    for line in csv.reader(raw_data):
        print(line)
        
#read csv data in the form of dictionary

import csv
with open('buzzers.csv') as raw_data:
    for line in csv.DictReader(raw_data):
        print(line)
        
###############################################################################

with open('buzzers.csv') as raw:
    dictionary={}
    for line in raw:
        key,value=line.split(',')
        dictionary[key]=value
dictionary

###############################################################################

#function within a function

def plus_one(number):
    def add_one(number):
        number1=number+1
        return number1
    result=add_one(number)
    return result
print(f"4+1={plus_one(4)}")

###############################################################################

def plus_one(number):
    result1=number+1
    return result1
def function_call(function):
    result=function(3)
    return result
function_call(plus_one)

###############################################################################

#Function returning another function
def hello_function():
    def say_hi():
        return "hi"
    return say_hi
hello=hello_function()
hello()

###############################################################################

#Need for decorators
import time
lst=[1,2,3,4,5,6,7,8,9,10]
def cube(numbers):
    start=time.time()
    result=[]
    for num in numbers:
        result.append(num*num*num)
    end=time.time()
    totalTime=(end-start)*1000
    print(f"Total execution time= {totalTime}")
    return result
cube(lst)

#Decorator : Passing Function In Argument
def say_hi():
    return "hello there"
def uppercase(function):
    def wrapper():
        func=function()
        make_uppercase=func.upper()
        return make_uppercase
    return wrapper
decorate=uppercase(say_hi)
decorate()

def uppercase(function):
    def wrapper():
        func=function()
        make_uppercase=func.upper()
        return make_uppercase
    return wrapper
@uppercase
def say_hi():
    return "hello there"
say_hi()

#Multiple Decorators
def split_string(function):
    def wrapper():
        func=function()
        splitted_string=func.split()
        return splitted_string
    return wrapper
def uppercase_decorator(function):
    def wrapper():
        func=function()
        make_uppercase=func.upper()
        return make_uppercase
    return wrapper
@split_string
@uppercase_decorator
def say_hi():
    return "hello there"
say_hi()

import time
def time_it(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        total_time=(end-start)*1000
        print(func.__name__+f" took{total_time}mil sec")
        return result
    return wrapper
@time_it
def square(numbers):
    result=[]
    for num in numbers:
        result.append(num*num)
    return result
def cube(numbers):
    result=[]
    for num in numbers:
        result.append(num*num*num)
    return result
array=range(1,100000)
sq=square(array)
cu=cube(array)

#Exception Handling
try:
    numerator=50
    denom=int(input("Enter The Denominator : "))
    print(numerator/denom)
    print("Division Performed Successfully!!!")
except ZeroDivisionError:
    print("Denominator As ZERO Is Not Allowed!!!")
except ValueError:
    print("Only INTEGERS Should Be Entered!!!")
except:
    print("Exception Occured!!!")

#Exception Using Else
try:
    numerator=50
    denom=int(input("Enter The Denominator : "))
    ans=(numerator/denom)
    print("Division Performed Successfully!!!")
except ZeroDivisionError:
    print("Denominator As ZERO Is Not Allowed!!!")
except ValueError:
    print("Only INTEGERS Should Be Entered!!!")
except:
    print("Exception Occured!!!")
else:
    print("The Result Of Divison Is : ",ans) #Will Be Executed If Ni Exception

#Exception Using Finally
try:
    numerator=50
    denom=int(input("Enter The Denominator : "))
    ans=(numerator/denom)
    print("Division Performed Successfully!!!")
except ZeroDivisionError:
    print("Denominator As ZERO Is Not Allowed!!!")
except ValueError:
    print("Only INTEGERS Should Be Entered!!!")
except:
    print("Exception Occured!!!")
else:
    print("The Result Of Divison Is : ",ans)
finally:
    print("OVER AND OUT") #It Will Be Compulsary Executed At Last


####################################OOP########################################
class Human:
    def __init__(self,n,o):
        self.name=n
        self.occupation=o
    def do_work(self):
        if self.occupation=='tennis player':
            print(self.name,"plays Tennis")
        elif(self.occupation=='actor'):
            print(self.name,"shoots films")
    def speaks(self):
        print(self.name,"says how are you")        
tom=Human('Tpm Cruise','actor')
tom.do_work()
tom.speaks()           

################################INHERITANCE####################################
#Single Inheritance
class Vehicle:
    def general_usage(self):
        print("General Use : Transportation")
class  car(Vehicle):
    def __init__(self):
        print("I Am Car!!!")
        self.wheels=4 
        self.has_roof=True
    def specific_usage(self):
        self.general_usage()
        print("Specific Use : Vacation")
class  bike(Vehicle):
    def __init__(self):
        print("I Am Bike!!!")
        self.wheels=2 
        self.has_roof=False
    def specific_usage(self):
        self.general_usage()
        print("Specific Use : Racing")   
c=car()
c.specific_usage()
b=bike()
b.secific_usage()         
  
#Multiple Inheritance
class Father():
    def skills(self):
        print("I Like Farming")
class Mother():
    def skills(self):
        print("I Like Cooking")
class Child(Father,Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("I Like Sports")
c=Child()
c.skills()
           
 
            
