import random

def add_population(population_length):
    population = []
    while population_length > 0:
        input_population = input('Enter the binary code: ')
        population.append(input_population)
        population_length -= 1

    return population

def fitness_calculation(chromosome, target):
    return sum(c1 == c2 for c1, c2 in zip(chromosome, target))

def fitness_proportionate(population, target):
    fitness_scores = [fitness_calculation(chromosome, target) for chromosome in population]
    total_fitness = sum(fitness_scores)

    selected_parents = []

    for _ in range(len(population)):
        random_number = random.uniform(0, total_fitness)
        probability = 0
        for i, fitness in enumerate(fitness_scores):
            probability += fitness
            if probability >= random_number:
                selected_parents.append(population[i])
                break

    return selected_parents

population = add_population(6)
print("Population:", population)
print("Selected Parents:", fitness_proportionate(population, '11011010'))
