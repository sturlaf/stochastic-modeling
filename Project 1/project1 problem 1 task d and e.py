# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 15:15:18 2019

@author: Sturla
"""
import numpy as np
import matplotlib.pyplot as plt
#from matplotlib import rc


T = 1000 #The total population
gamma = 0.20 #Probability og becomming immune

def beta(I : int) -> float:
    '''Calculates the new probability for each iteration.'''
    return 0.5*I/T

def increment_time(S : int, I : int, R : int):
    '''Runs one iteration of the process.'''
    #Pick the number of new infected and immune by a binomial distubution.
    new_infected = np.random.binomial(S, beta(I))
    new_immune = np.random.binomial(I, gamma)
    
    S -= new_infected
    R += new_immune
    I += (new_infected - new_immune)
    return S, I, R


def simulation() -> list:
    '''Simulates the markovchain using the given probabilities'''
    time_steps = []
    time_steps.append([950, 50, 0])
    for i in range(0, 200):
        S, I, R = increment_time(time_steps[i][0], time_steps[i][1], time_steps[i][2])
        time_steps.append([S, I, R])   
    return time_steps
    

def simulation_max_infected(initial_conditions : list):
    ''' 
    Simulates the markov chain, and keeps track of the max number of
    infected, and the number uf iterations untill max is reached
    '''
    time_steps = []
    time_steps.append(initial_conditions)
    
    max_infected = initial_conditions[1]
    index = 0
    for i in range(0, 200):
        S, I, R = increment_time(time_steps[i][0], time_steps[i][1], time_steps[i][2])
        if I > max_infected:
            max_infected = I
            index = i   
        elif I == 0:
           break
        time_steps.append([S, I, R])
    return max_infected, index

def calc_avrage_max():
    '''
    Simulates the process 1000 times, and returns the avarge max, and the
    avarge iterations untill max is reached.
    '''
    max_list = []
    time_list = []
    for i in range(1000):
        max_infected, time = simulation_max_infected([950, 50, 0])
        max_list.append(max_infected)
        time_list.append(time)
    return np.average(max_list), np.average(time_list)  

max_infected, time_of_max = calc_avrage_max()

print("e)")
graph = np.array(simulation())
# use LaTeX fonts in the plot
#plt.rc('text', usetex=True)
#plt.rc('font', family='serif')
 
# plot
plt.plot(graph)
# set labels (LaTeX can be used)
#plt.title(r'\textbf{Mutual Information Feature Selection}', fontsize=11)
#plt.xlabel(r'\textbf{Time (days)}', fontsize=11)
#plt.ylabel(r'\textbf{People}', fontsize=11)
plt.ylabel('People')
plt.xlabel('Time (days)')
plt.title("The number of people in each state", fontdict={'fontname': 'Times New Roman', 'fontsize': 21}, y=1.03)
plt.show()
print("f)")
print("Max number of infected: " , max_infected)
print("Time untill max: " ,time_of_max)