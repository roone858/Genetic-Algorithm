import random
import datetime


def equation(x, y, z):
    return 6*x**3 + y**2 + 90*z - 25


def init_population(numOfPopulation):
    parents = []
    for i in range(numOfPopulation):
        parents.append((random.uniform(0, numOfPopulation), random.uniform(
            0, numOfPopulation), random.uniform(0, numOfPopulation)))
    return parents


def calc_fitness(x, y, z):
    ans = equation(x, y, z)
    return 99999 if ans == 0 else abs(1/ans)


def findBestSolutions(population):
    bestParents = [
        (calc_fitness(parent[0], parent[1], parent[2]), parent) for parent in population]
    bestParents.sort(reverse=True)
    return bestParents[:100]


def crossover(parent_1, parent_2):
    m = random.randrange(0, 3)
    child_1 = parent_1[:m] + parent_2[m:]
    child_2 = parent_2[:m] + parent_1[m:]
    return child_1, child_2, parent_1, parent_2


def mutate(child):
    m = random.randrange(0, 3)
    child = list(child)
    child[m] = child[m]*random.uniform(0.99, 1.01)
    return tuple(child)


solutions = init_population(1000)
g = 0
while True:
    bestSolutions = findBestSolutions(solutions)
    newGeneration = []
    for i in range(0, len(bestSolutions), 2):

        child1, child2, parent1, parent2 = crossover(
            bestSolutions[i][1], bestSolutions[i+1][1])
        child1, child2 = mutate(child1), mutate(child2)
        newGeneration.extend((parent1, parent2, child1, child2))

    solutions = newGeneration
    print(f"\r gen = {g+1:06} -bestFitness={bestSolutions[0][0]}", end="")
    if bestSolutions[0][0] > 999:
        print("\n", bestSolutions[0][1])
        break
    g += 1
