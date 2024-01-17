import random

#Step1:Initialization
def initialize_population(population_size, x_range):
    population = []
    for _ in range(population_size):
        x_value = random.uniform(x_range[0], x_range[1])
        population.append(x_value)
    return population


#Step2:Fitness Function
def fitness_function(chromosome):
    return -chromosome ** 2


#Step3:Selection
#selecting parent from thr population
def paranet_selection(population, fitness_function, tournament_size):
    selected_parent = []
    for _ in range(len(population)):
        tournament = random.sample(population, tournament_size)
        winner = max(tournament, key=fitness_function)
        selected_parent.append(winner)

    return selected_parent


#Step4:Crossover(single-Point Crossover)
def  single_point_crossover(parent1, parent2):
    crossover_point = random.randint(0, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2



#Step5:Mutation






