#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import math
# Fitness function. The code maximizes the value of the fitness function
def rosenbrock_func(x_local):
    D=x_local.size     # size of Numpy vector x_local
    rosenbrock_i=[0]
    for i in range(D-1):
       rosenbrock_i += ( 100 * ((x_local[i + 1] - x_local[i]**2)**2) + (x_local[i] - 1)**2 )
    return rosenbrock_i

x_local=np.array([2,3,4,5])
b=rosenbrock_func(x_local)
print (b)


# In[ ]:





# In[ ]:




