import random
import datetime

geneSet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."
target = "Hello World!"


def generate_parent(length):
    genes = []
    while len(genes) < length:
        sampleSize = min(length - len(genes), len(geneSet))
        genes.extend(random.sample(geneSet, sampleSize))
    print(genes)  # random.sample return list so we use extend
    return ''.join(genes)


def calc_fitness(guess):
    return sum(1 for x, y in zip(target, guess) if x == y)


def mutate(parent):
    index = random.randrange(0, len(parent))
    childGenes = list(parent)
    newGene, alternate = random.sample(geneSet, 2)
    if newGene == childGenes[index]:
        childGenes[index] = alternate
    else:
        childGenes[index] = newGene
    return ''.join(childGenes)


def display(guess):
    timeDiff = datetime.datetime.now() - startTime
    fitness = calc_fitness(guess)
    print("{0}\t{1}\t{2}".format(guess, fitness, str(timeDiff)))


random.seed()
startTime = datetime.datetime.now()
parent = generate_parent(len(target))
parentFitness = calc_fitness(parent)
# i=0
while True:
    #    print(i)
    child = mutate(parent)
    child_Fitness = calc_fitness(child)
    #   i=i+1
    if parentFitness >= child_Fitness:
        continue
    display(child)
    if child_Fitness >= len(parent):
        break
    parentFitness = child_Fitness
    parent = child
