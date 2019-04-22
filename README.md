# Example of the application of a genetic algorithm

This is an implementation of the example "Robby" found in the book:

Complexity a guided tour by Melanie Mitchell. 
The script is an implementation of fa Genetic Algorithm to solve the problem as proposed in the book (p 131)

![Complexity](https://books.google.se/books/about/Complexity.html?id=bbN-6aDFrrAC&redir_esc=y)

The problem consists of an imaginary robot called Robby, who has to navigate across a board in which there are some cans. 
The objective is to find the best route in which the robot can pick all the cans. For this purpose a Genetic Algorithm is implemented as follows:

```
1. An initial population of candidate solutionsis genetared randomly. 
2. The fitness of eac individual in the current population is calculated
3. Some number of indivuduals with the highest scores are selected to be the parents of the next generation
4. Crossover is performed with pairs of the selected individuals until a new population with the same amounf of individuals as the original is created
5. Go to sstep 2.
```

![Robby](picture)
