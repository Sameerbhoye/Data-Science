# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 08:49:20 2024

@author: samir
"""

import matplotlib.pyplot as plt
X=range(1,50)
Y=[value * 3 for value  in X]
print("value of X:")
print(*range(1,50))
'''
this is equivalent to -
i in range (1,50):
print(i,end= ' ')
'''
print("values of y (thrice of x):")
print(Y)
#plot lines and / or makers to the axes 
plt.plot(X,Y)
#
plt.xlabel('x - axis ')
plt.ylabel('y - axis ')
plt.title('Draw a line.')
plt.show()
#########################################

import matplotlib.pyplot as plt
x= [1,2,3]
y= [2,4,1]
# plot lines and / or 
plt.plot(x,y)
#set the x axis label of the current axis 
plt.xlabel('x - axis')
#set the y axis label of the current axis 
plt.ylabel('y - axis ')
#set a title 
plt.title('Sample  graph!')
#Display a figure 
plt.show()

import matplotlib.pyplot as plt
#
x1=[10,20,30]
y1=[20,40,10] 


x2=[10,20,30]
y2=[40,10,30] 
plt.plot(x1, y1 , label= "line 1")
#
plt.plot(x2, y2, label= "line 2")
#
plt.xlabel('x -axis')
#
plt.ylabel('y- axis')
#
plt.title('Two or more lines on same plot with suitable ')
#
plt.legend()
#
plt.show()

################################################


import matplotlib.pyplot as plt
#
x1=[10,20,30]
y1=[20,40,10] 


x2=[10,20,30]
y2=[40,10,30] 

plt.plot(x1, y1 ,color='blue',linewidth=3,  label= "line 1")
#
plt.plot(x2, y2,color= 'red',linewidth=5, label= "line 2")
#
plt.xlabel('x -axis')
#
plt.ylabel('y- axis')
#
plt.title('Two or more lines on same plot with suitable ')
#
plt.legend()
#show a legend on the plot 
plt.show()


import matplotlib.pyplot as plt
#
x1=[10,20,30]
y1=[20,40,10] 


x2=[10,20,30]
y2=[40,10,30] 

plt.plot(x1, y1 ,color='blue',linewidth=3,  label= "line1-dotted",linestyle='dotted')
#
plt.plot(x2, y2,color= 'red',linewidth=5, label= "line2-dashed",linestyle='dashed')
#
plt.xlabel('x -axis')
#
plt.ylabel('y- axis')
#
plt.title('Two or more lines on same plot with suitable ')
#
plt.legend()
#show a legend on the plot 
plt.show()
  
######
import matplotlib.pyplot as plt
#
x=[1,2,3,4,5]
y=[2,6,3,6,3]
#
plt.plot(x,y, color= 'red',linestyle= 'dashdot', linewidth=3
         ,marker= 'o', markerfacecolor='blue', markersize=12)
plt.ylim(1,8)
plt.xlim(1,8)
plt.xlabel('x- axis')
plt.ylabel('y- axis ')
plt .title('Display marker')
plt.show()

import matplotlib.pyplot as plt
x=['java','python', 'php','javascript','c#','c++']
popularity=[22.2,17.6,8.8,8,7.7,6.7]
x_pos=[i for i, _ in enumerate(x)]
plt.bar(x_pos, popularity, color='blue')
plt.xlabel("languages")
plt.ylabel("popualarity")
plt.title("popularity of programming languages \n "+
          "worldwide, oct 2017 compared t a year ago ")
plt.xticks(x_pos, x)
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5',color='red')
plt.show()

import matplotlib.pyplot as plt
x=['java','python', 'php','javascript','c#','c++']
popularity=[22.2,17.6,8.8,8,7.7,6.7]
x_pos=[i for i, _ in enumerate(x)]
plt.barh(x_pos, popularity, color='green')
plt.xlabel("languages")
plt.ylabel("popualarity")
plt.title("popularity of programming languages \n "+
          "worldwide, oct 2017 compared t a year ago ")
plt.yticks(x_pos, x)
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5',color='blue')
plt.show()

import matplotlib.pyplot as plt
x=['java','python', 'php','javascript','c#','c++']
popularity=[22.2,17.6,8.8,8,7.7,6.7]
x_pos=[i for i, _ in enumerate(x)]
plt.bar(x_pos, popularity)
plt.xlabel("languages")
plt.ylabel("popualarity")
plt.title("popularity of programming languages \n "+
          "worldwide, oct 2017 compared t a year ago ")
plt.xticks(x_pos, x)
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5',color='red')
plt.show()


import matplotlib.pyplot as plt
x=['java','python', 'php','javascript','c#','c++']
popularity=[22.2,17.6,8.8,8,7.7,6.7]
x_pos=[i for i, _ in enumerate(x)]
plt.bar(x_pos, popularity, color=['red','blue','black','green','yellow','cyan'])
plt.xlabel("languages")
plt.ylabel("popualarity")
plt.title("popularity of programming languages \n "+
          "worldwide, oct 2017 compared t a year ago ")
plt.xticks(x_pos, x)
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5',color='red')
plt.show()

import matplotlib.pyplot as plt
blood_sugar=[113,85,90,150,149,88,93,115,135,80,77,82,129]
#plt.hist(blood_sugar, rwidth=0.8 )
plt.hist(blood_sugar, rwidth=0.5,bins=4)

plt.xlabel("sugar level")
plt.ylabel("Number of patients")
plt.title("Blood sugar chart")
plt.hist(blood_sugar, bins=[80,100,125,150], rwidth=0.95, color='green')

import matplotlib.pyplot as plt
import numpy as np
np.random.seed(10)
data=np.random.normal(100,20,200)
fig=plt.figure(figsize=(10,7))
plt.boxplot(data)
plt.show()

import matplotlib.pyplot as plt
import numpy as np


np.random.seed(10)
data1=np.random.normal(100,10,200)
data2=np.random.normal(90,20,200)
data3=np.random.normal(80,30,200)
data4=np.random.normal(70,40,200)
data=[data1,data2, data3, data4]
fig=plt.figure(figsize=(10,7))
ax=fig.add_axes([0,0,1,1])
bp=ax.boxplot(data)





