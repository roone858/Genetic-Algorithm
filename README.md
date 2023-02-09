# Genetic Algorithm
Genetic algorithms simulate the process of natural selection which means those species who can adapt to changes in their environment are able to survive and reproduce and go to next generation. In simple words, they simulate “survival of the fittest” among individual of consecutive generation for solving a problem. Each generation consist of a population of individuals and each individual represents a point in search space and possible solution. Each individual is represented as a string of character/integer/float/bits. This string is analogous to the Chromosome.
# Canonical Genetic Algorithm
- GA starts with an initial population whose elements are called 
chromosomes. 
-  The chromosome consists of a fixed number of variables which are 
called genes.
-  In order to evaluates and rank chromosomes in a population, a 
fitness function based on the objective function should be defined. 
-  Three operators must be specified to construct the complete 
structure of the GA procedure
- Selection – Crossover - Mutation

# Genetic Algorithm operations 

1. Initialization: Create an initial population of randomly generated solutions to a given problem (often called chromosomes or individuals).

2. Fitness Function: Measure the “fitness” of each individual in the population by evaluating its performance against a predefined criterion (usually this criterion is linked to the goal of the overall problem).

3. Selection: Create a mating pool by selecting individuals from the current population in accordance with their fitness. 

4. Crossover: Combine pairs of selected individuals to create new offspring in the next generation, swapping genetic material between them (often using specific crossover points on their chromosomes). 

5. Mutation: Introduce random variations into the population by making small changes to some of the offspring's genetic material (chromosomes) during the crossover process. 

6. Replacement: Replace worse performing members of the current population with newly created offspring from preceding steps, creating a new generation of solutions. 

7. Repeat: Go back to step 2 and repeat until either good enough solutions are found or a pre-defined number of generations has been reached.

# Representation of Solutions
- Each chromosome represents a point in search space. 
- A chromosome consists of several genes, where the gene is the 
functional unit of inheritance. 
- Each gene represents one characteristic of the individual. 
- In terms of optimization, a gene represents one parameter of the 
optimization problem.
- A very important step in the design of an EA is to find an 
appropriate chromosome representation.
