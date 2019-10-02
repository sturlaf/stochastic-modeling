# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 16:20:45 2019

@author: Sturla
"""

import numpy as np
import matplotlib.pyplot as plt


days = 59 #Days between 1.jan - 1.mars
lambd = 1.5 #The parameter in the poisson process

def sim_poisson():
    '''Simulates the poisson process'''
    process_time_steps = []
    value = 0
    for i in range(days):
        value += np.random.poisson(lambd)
        process_time_steps.append(value)
    return np.array(process_time_steps)

#Simulate the poisson process 10 times
for i in range(10):
    plt.plot(sim_poisson())
plt.title("10 realizations of the Poisson Process", fontdict={'fontname': 'Times New Roman', 'fontsize': 21}, y=1.03)
plt.ylabel('Number of claims')
plt.xlabel('Time (days)')
plt.ylim(0)
plt.xlim(0)
plt.show()

def count_large():
    '''
    Counts how many times the process reaches above 100 in 1000 iterations,
    and returns the percentage of times this happens.
    '''
    count = 0
    for i in range(1000):
        sim = sim_poisson()
        sim_max = sim[-1]
        if sim_max > 100:
            count += 1
    return float(count)/1000
    
print("The precentage of iterations larger than 100 is: " + str(count_large())) 
    
def expected_claim_and_var():
    '''Returns the excpected number of claims'''
    realization = []
    for i in range(1000):
        time_steps = sim_poisson()
        last_time_step = time_steps[-1]
        Z = 0
        for j in range(last_time_step):
            C = np.random.exponential(1/10)
            Z += C
        realization.append(Z)
    return np.average(realization), np.var(realization)

excepcted_claims_value, estimated_variance = expected_claim_and_var()
print("The excpected value of the claims is: " + str(excepcted_claims_value))
print("The estimated variance of the claims is: " + str(estimated_variance))    