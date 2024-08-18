# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 08:43:41 2024

@author: samir
"""
#arrays in numpy
import numpy as np
arr=np.array([10,20,30])
print(arr)
#v=create a multi dimensional array
#
arr=np.array([[10,20,30],[40,50,60]])
print(arr)
#represent a minimum dimensions
#use ndmin param to specify how many minimum dimensions you want to create with minimum dimensions
arr=np.array([10,20,30,40],ndmin=3)
print(arr)
#change the datatype
#dtype parameter
arr=np.array([10,20,30],dtype=complex)
print(arr)
#Get the Dimensions of Array
#
arr=np.array([[1,2,3,4],[7,8,6,7],[9,10,11,12],[13,14,15,16]])
print(arr.ndim)
print(arr)
#
#
arr=np.array([10,20,30])
print("Each item contain",arr.itemsize)

arr=np.array([[10,20,30],[40,50,60]])
print(arr.size)
print(arr.shape)

arr=np.array([10,20,30])
print("array",arr)

arr=np.array([[10,20,30],[40,50,60]],dtype='float')
print("array created by using list:\n ",arr)

#create a sequence of integers using arange()
#A sequential array with step of 3
arr=np.arange(0,20,3)
print("A sequential array with steps of 3: \n",arr)

arr=np.arange(11)
print(arr)
print(arr[2])
print(arr[-2])
print(arr[-5])

arr=np.array([[10,20,30,40,50],[50,60,70,80,90]])
print(arr.shape)
print(arr[1,1])
print(arr[0,4])
print(arr[1,-1])

#Accessing arrayy elements using Slicing 
arr=np.array([0,1,2,3,4,5,6,7,8,9])
x=arr[1:8:2]#start :end :in step of 2
print(x)

x=arr[-2:3:-1]#start last but one(-2) upto 3 but not 3
print(x)

x=arr[-2:10]
print(x)

mul_arr=np.array([[1,2,3,4],[7,8,6,7],[9,10,11,12],[13,14,15,16]])
print(mul_arr[1,2])
print(mul_arr[1,:])
print(mul_arr[:,1])

x=mul_arr[:3,::2]
print(x)
#interger array indexing 
arr=np.arange(35).reshape(5,7)
print(arr)

import numpy as np
arr=np.arange(12).reshape(3,4)
print(arr)
rows=np.array([False,True,True])#not 0th row only 1st and 2nd rows 
rows
wanted_rows=arr[rows,:]
print(wanted_rows)

#Use asarray()
list=[20,30,40,50]
array=np.asarray(list)
print("array",array)
print(type(array))

#shape
array=np.array([[1,2,3],[4,5,6]])
array
print(array.shape)

#resize the array 
array=np.array([[1,2,3],[4,5,6]])
array.shape=(3,2)
print(array)

#using reshape()
array=np.array([[1,2,3],[4,5,6]])
n_array=array.reshape(3,2)
print(n_array)

arr1=np.arange(16).reshape(4,4)
arr2=np.array([1,2,3,4])

add_arr=np.add(arr1,arr2)
print(f"Adding two numbers : \n{add_arr}")

sub_arr=np.subtract(arr1,arr2)
print(f"Subtracting  two numbers : \n{sub_arr}")

mul_arr=np.multiply(arr1,arr2)
print(f"Multiplying  two numbers : \n{mul_arr}")

div_arr=np.divide(arr1,arr2)
print(f"Dividing two arrays  two numbers : \n{div_arr}")

#to perform reciprocal operation
arr1=np.array([50,10.3,5,1,200])
rep_arr1=np.reciprocal(arr1)
print(rep_arr1)

#to perform power operation 
arr1=np.array([3,10,5])
pow_arr1=np.power(arr1,3)
print(pow_arr1)

arr2=np.array([3,2,1])
print("My second array : \n",arr2)
pow_arr2=np.power(arr1,arr2)
print("After applying power function to array:\n",pow_arr2)

import numpy as np
arr1=np.array([7,20,13])
arr2=np.array([3,5,2])
arr1.dtype
mod_arr=np.mod(arr1,arr2)
print("After applying mod function to array : \n",mod_arr)

#create empty array
from numpy import empty
a=empty([3,3])
print(a)

#create zero array
from numpy import zeros
a=zeros([3,5])
print(a)

np.__version__

#create one array
from numpy import ones
a=ones([5])
print(a)

#create array with vstack
from numpy import array,vstack
a1=array([1,2,3])
print(a1)
a2=array([4,5,6])
print(a2)
#vertical stack
a3=vstack((a1,a2))
print(a3)
print(a3.shape)

#create array with hstack
from numpy import array,hstack
a1=array([1,2,3])
print(a1)
a2=array([4,5,6])
print(a2)
#vertical stack
#create horizonatal stack
a3=hstack((a1,a2))
print(a3)
print(a3.shape)

from numpy import array
#define array
data=array([10,20,30,40,50])
#array index 
print(data[5])
#IndexError: index 5 is out of bounds for axis 0 with size 5

from numpy import array
data=array([[11,22],[33,44],[55,66]])
print(data[0,])# 0th row and all columns
#[11 22]

from numpy import array
#define array
data=array([11,22,33,44,55])
print(data[-2:])
###############################
#split input and outut data
from numpy import array
#define array
data=array([[11,22,33],[44,66,77],[55,88,99]])
X,y=data[:,:-1],data[:,-1]
X
y
#data[:,-1] -all rows and columns 0 and 1 
#all rows and last column

from numpy import array
#
a=array([1,2,3])
print(a)
#
b=2
print(b)
c=a+b
print(c)

#vector L1 norm 
# The L1 norm is calculated as the sum of the absolute vector values 
#where the absolute value value of a scalar uses the noataion |a1|.
# in effect the norm is calculation of the Manhattan distance from 
#from the origin of vector space.
#||v1|| 1= |a1|+ |a2|+|a3|
from numpy import array
from numpy .linalg import norm
#define array
a=array([1,2,3])
print(a)
l1=norm(a,1)
print(l1)

''' 
'''
from numpy import array
from numpy .linalg import norm
#define array
a=array([1,2,3])
print(a)
#calculate norm 
l2=norm(a)#1+4+9=14 under root of 14 is 3.7416573867739413
print(l2)
#######################################

from numpy import array,tril,triu
#define square matrix
m=array([[1,2,3],[4,5,6],[7,8,9]])
print(m)
#lower triangular matrix
lower=tril(m)
print(lower)
#upper triangular matrix
upper=triu(m)
print(upper)

from numpy import array, diag
# 
m= array([[1,2,3],[1,2,3],[1,2,3]])
print(m)
#create diagonal matrix from vector
d=diag(m)
print(d)
D=diag(d)
print(D)

#identity matrix
from numpy import identity
i =identity(3)
print(i)

#orthogonal matrix
from numpy import array
from numpy.linalg import inv 
Q= array([[1,0],[0,1]])
print(Q)
v=inv(Q)
print(Q.T)
print(v)
I=Q.dot(Q.T)
print(I)


###########
from numpy import array
#define array 
a=array([[1,2],[3,4],[5,6]])
print(a)
#claculate transpose
c=a.T
print(c)

#inverse of matrix
from numpy import array
from numpy.linalg import inv
#
a=array([[1.0,2.0],[3.0,4.0]])
print(a)
b=inv(a)
print(b)
#multiply a and b 
i=a.dot(b)
print(i)

from numpy import array
from scipy.sparse import csr_matrix
#create dense method 
a=array([[1,0,0,1,0,0],[0,0,2,0,0,1],[0,0,0,2,0,0]])
print(a)
#convert to sparse matrix (csr method )
s=csr_matrix(a)
print(s)
#reconstruct dense matrix
b=s.todense()
print(b)





















