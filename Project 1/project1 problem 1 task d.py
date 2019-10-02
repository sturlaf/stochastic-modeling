# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 14:43:36 2019

@author: Sturla
"""
import numpy as np

#The transition probabilities:
beta = 0.05 #Probability of becomming infected
gamma = 0.20 #Probability og becomming immune

def pick_state(state: int) -> int:
    ''' 
    This function chooses the next state, given the state it is currently in
    accordig to the transition probabilities.
    
    param: 
        state - the state the procses is currently in.
    return: 
        the next state.
    '''
    if state == 0:
        prob = beta
    elif state == 1:
        prob = gamma
    else: 
        return 2
    if np.random.uniform() >  prob:
        return state
    else:
        return state + 1
    
def markov():
    '''
    This method simulates the markovchain for 1000 iterations.
    
    return: 
        the number of iterations before reaching state 2, 
        and the number of times in state 0.
    '''
    state = 0 #The initial state
    state0_time = 1 #The number of times the proscess is in state 0
    nr_untill_state2 = 0 #The number of iterations before reaching state 2, wich is an absorbing state
    while state != 2:
        nr_untill_state2 += 1
        state = pick_state(state)
        if state == 0:
            state0_time += 1
    return nr_untill_state2, state0_time

    
def calc_avrage_times():
    '''
    Simulates the markovchain 1000 times, and returns the avrage 
    number of times in state 0, and in state 1.
    
    return: 
        the avrage number of times in state 0 and state 1.
    '''
    state0_times = []
    nr_infected_to_recovered = []
    for n in range(1000): #Calculate 1000 simulations
        nr_untill_state2, state0_time = markov()
        #Append the number of times the chain is in state 1
        nr_infected_to_recovered.append(nr_untill_state2 - state0_time)
        state0_times.append(state0_time)   
    return np.average(state0_times), np.average(nr_infected_to_recovered), 
    
#Calculate the suspected number of iterations in state 0, and in state 1
suspected_state0_time, suspected_state1_time = calc_avrage_times();
print("a)")      
print("The average time in state 0 is: " + str(suspected_state0_time)) 
print("The average time in state 1 is: " + str(suspected_state1_time))