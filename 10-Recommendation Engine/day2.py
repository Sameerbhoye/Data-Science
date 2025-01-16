# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 08:56:30 2024

@author: dell
"""

"""9-10-2024"""


############################

import numpy as np
import matplotlib.pyplot as plt


#target value (true value)
true_value=50

#simulate data
#1 acuutrate and precise (close to true and tightly grouped)
'''
Loc=true value (True Value 58): The values will be
 centered around the true value (50).

scale 1: The standard deviation (spread) is small,
meaning the values will be tightly grouped around the true value. 
This toplies high precision. 
The measurements will vary only a Little from the true value, 
so they'll be both accurate (close to 50) and

precise (close to each other).

'''

accurate_precise=np.random.normal(loc=true_value,scale=1,size=10)

# 2. accurate but not precise(close to value but not spred out)

accurate_not_precise=np.random.normal(loc=true_value,scale=10,size=10)

'''
The two Lines of code you've highlighted may Loos similar,
 but they differ in one smportant aspect: the value of scale, 
 which controls the spread of the generated values around 
 the true value (loc).

'''


# 3.precise but not accurate (far true values but tightly grouped)

precise_not_accurate=np.random.normal(loc=70,scale=1,size=10)

# 4. neither accurate nor precise (far true value and spred out)

not_accurate_not_precise=np.random.normal(loc=70,scale=10,size=10)


#plotting the result
plt.figure(figsize=(10,6))

plt.scatter(accurate_precise,[1]*10,color='green',
            label='Accurate and precise')


# plot 2 accurate but not precise

plt.scatter(accurate_not_precise,[2]*10,color='blue',
            label='Accurate and not precise')

#plot 3 precise but not precise

plt.scatter(precise_not_accurate,[3]*10,color='orange',
            label='precise not accurate')


# plot 4 neither accurate not precise
plt.scatter(not_accurate_not_precise,[4]*10,color='red',
            label='not Accurate and not precise')

#adding target line

plt.axvline(true_value,color='black',linestyle='---',
            label="True Value")
#label and legend

plt.yticks([1,2,3,4],['Accurate and Precise','Accurate but not precise',
                      'precise but not accurate','neither accurate nor precise'])


plt.xlabel('Measurment Value')
plt.legend()
plt.title('Accuracy and Precision Demostration')

plt.show()






