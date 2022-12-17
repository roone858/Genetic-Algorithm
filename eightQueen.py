from numpy import random
import numpy as np


def init_pop(rows):
    return random.randint(8, size=(rows, 8))


def calc_fitness(population):
    fitnessValues = []
    for x in population:
        penalty = 0
        for i in range(len(x)):
            r = x[i]
            for j in range(8):
                if i == j:
                    continue
                d = abs(i - j)
                if x[j] in [r, r - d, r + d]:
                    penalty += 1
        fitnessValues.append(penalty)
    # print("population is :\n", population)
    # print("fitness values is : \n", -1 * np.array(fitnessValues))
    return -1 * np.array(fitnessValues)


def selection(populations, fitness_values):
    nega = (np.abs(min(fitness_values) - 1)) + np.array(fitness_values)
    probs = [num / sum(nega) for num in nega]
    # print("negative value of fitness  is : \n", nega)
    # print("probs is : \n", probs)
    n = len(populations)
    return populations[np.random.choice(np.arange(n), size=n, p=probs)]


def crossover(parent_1, parent_2, pc):
    r = np.random.random()
    if r < pc:
        m = np.random.randint(1, 8)
        child_1 = np.concatenate([parent_1[:m], parent_2[m:]]) # single point cross over
        child_2 = np.concatenate([parent_2[:m], parent_1[m:]])
    else:
        child_1 = parent_1.copy()
        child_2 = parent_2.copy()
    # print("child1:", child_1)
    # print("child2:", child_2)
    return child_1, child_2


def mutation(child, pm):
    r = np.random.random()
    if r < pm:
        m = np.random.randint(8)
        child[m] = np.random.randint(8)
    return child


def crossover_mutation(parents, pc, pm):
    new_pop = np.empty((len(parents), 8), dtype=int)
    n = len(parents)
    for i in range(0, n, 2):
        childOne, childTow = crossover(parents[i], parents[i + 1], pc)
        new_pop[i] = childOne
        new_pop[1 + i] = childTow
    for i in range(len(new_pop)):
        mutation(new_pop[i], pm)
    return new_pop


def eightQueen(popSize, max_generation, pc, pm):
    population = init_pop(popSize)
    bestFitnessOverall = None
    best_solution = []
    for i in range(max_generation):
        fitnessValues = calc_fitness(population)
        bestIndex = fitnessValues.argmax()
        bestFitness = fitnessValues[bestIndex]
        if bestFitnessOverall is None or bestFitness > bestFitnessOverall:
            bestFitnessOver = bestFitness
            best_solution = population[bestIndex]
        print(f"\r gen = {i+1:06} -bestFitness={bestFitness:02}", end="")
        if bestFitness == 0:
            print("\nbest solution is founded")
            break
        selected_population = selection(population, fitnessValues)
        population = crossover_mutation(selected_population, pc, pm)
    print(best_solution)


eightQueen(100, 10000, 0.7, 0.5)
