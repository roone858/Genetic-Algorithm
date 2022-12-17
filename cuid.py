import random


def equation(x, y, z):
    return 6*x**3 + y**2 + 90*z - 25


solutions = []
noOfSolution = 1000
for s in range(noOfSolution):
    solutions.append((random.uniform(0, noOfSolution), random.uniform(
        0, noOfSolution), random.uniform(0, noOfSolution)))


def fitness(x, y, z):
    ans = equation(x, y, z)
    if ans == 0:
        return 99999
    else:
        return abs(1/(1+ans))


iteration = 1000
for i in range(iteration):
    parents = [(fitness(s[0], s[1], s[2]), s)
               for s in solutions]

    parents.sort(reverse=True)
    bestSolutions = parents[:100]
    xP = [s[1][0] for s in bestSolutions]
    yP = [s[1][1] for s in bestSolutions]
    zP = [s[1][2] for s in bestSolutions]

    newGen = [(random.choice(xP)*random.uniform(0.99, 1.01),
               random.choice(yP)*random.uniform(0.99, 1.01),
               random.choice(zP)*random.uniform(0.99, 1.01)) for _ in range(noOfSolution)]

    solutions = newGen
    print("{0}\t{1}".format(i, bestSolutions[0]))
    if bestSolutions[0][0] > 999:
        break
