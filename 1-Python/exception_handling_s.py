# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 09:00:37 2024

@author: samir
"""

numerator=50
try:
    denominator=int(input("Enter the Denominator:"))
    result=numerator/denominator
    print(f"Division is : {result}")
except ZeroDivisionError:
    print("Division by Zero is not allowed ")
except ValueError:
    print("only integers should be entered !")
    
#############################################################################################################

#Any error in general

numerator=50
try:
    denominator=int(input("Enter the Denominator:"))
    result=numerator/denominator
    print(f"Division is : {result}")
    print("abc"+23)
except ZeroDivisionError:
    print("Division by Zero is not allowed !")
except ValueError:
    print("only integers should be  entered !")
except:
    print("Some error occured !")

#################################################################################################################

#exception with try, except and else block

numerator=50
try:
    denominator=int(input("Enter the Denomiator:"))
    result=numerator/denominator
    print("Division perfomed successfully ")
except ZeroDivisionError:
    print("Division by Zero is not allowed !")
except ValueError:
    print("only intergers should be entered !")
else:
    print(f"Division is {result}")
    

#Finally block

numerator=50
try:
    denominator=int(input("Enter the Denominator :"))
    result=numerator/denominator
    print("Division performed successfully ")
except ZeroDivisionError:
    print("Division by Zero is not allowed !")
except ValueError:
    print("only integers should be entered !")
else:
    print(f"Division is {result}")
finally:
    print("OVER AND OUT !")

























    