#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 23:28:41 2018

@author: jl
"""

from Roby_generator import*
import matplotlib.pyplot as plt


"""
This is an implementation of the example "Robby" found in the book:

Complexity a guided tour by Melanie Mitchell. 
The script is an implementation of fa Genetic Algorithm to solve the problem as proposed in the book (p 131)

"""

# number of different 'individuals' in the initial population of instructions
population = 100
#  number of instructions that each individual will have
num_instruct = 200
# number of generations to iterate
generations = 600
# size of the board
siz = 10
# Generates a Board, with X number of obstacles, by default 10
amount_of_cans = 10
[w, p] = Board(siz, amount_of_cans)
# generates a population of N individuals with S number of instructions each one
pop_i = pop_generator(population, num_instruct)
# implements the genetic algorithm
mutation_rate = 0.4
[evaluation_last, best_results, average, worst, best_indiv] = gen_algot(pop_i, w, Robby, generations, mutation_rate)

# ========================FIGURES========================

plt.figure(1)
plt.plot(best_results, '-*g', label='worst individual')
plt.plot(average, '-+b', label='average')
plt.plot(worst, '-or', label='best individual')
plt.xlabel(['Time'])
plt.ylabel(['Fitnes'])
plt.legend(loc='best')
plt.show()

visualzation(best_indiv[-1], p, len(w))
