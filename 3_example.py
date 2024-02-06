import random

def initialize_population(population_size, x_range):
    population = []
    for _ in range(population_size):
        value = random.uniform(x_range[0], x_range[1])
        population.append(value)
    return population

def fitness_function(x):
    f_x = x**2 + 6*x + 9  
    return f_x



def parent_selection(population, fitness_function, tournament_size):
    selected_parents = []
    for _ in range(len(population)):
        tournament = random.sample(population, tournament_size)
        winner = max(tournament, key=fitness_function)
        selected_parents.append(winner)

    return selected_parents



def single_point_crossover(parent1, parent2):

    crossover_point = random.randint(0, 1)
    child1 = parent1 * (1 - crossover_point) + parent2 * crossover_point
    child2 = parent2 * (1 - crossover_point) + parent1 * crossover_point
    return child1, child2


def mutate(individual, mutation_rate):
    mutated_value = individual + mutation_rate * random.uniform(-1, 1)
    return mutated_value



population_size = 6
x_range = (-5, 5)
tournament_size = 3
mutation_rate = 0.1
num_generations = 50


population = initialize_population(population_size, x_range)

for generation in range(num_generations):
    #fitness
    fitness_values = [fitness_function(x) for x in population]

    # Parent selection
    selected_parents = parent_selection(population, fitness_function, tournament_size)

    # Crossover
    offspring = []
    for i in range(0, len(selected_parents), 2):
        parent1 = selected_parents[i]
        parent2 = selected_parents[i + 1]
        child1, child2 = single_point_crossover(parent1, parent2)
        offspring.extend([child1, child2])

    # Mutation
    for i in range(len(offspring)):
        offspring[i] = mutate(offspring[i], mutation_rate)

    # Combine parents and offspring 
    new_generation = selected_parents + offspring


    best_individual = max(new_generation, key=fitness_function)
    print(f"Generation {generation + 1}, Best Individual: {best_individual}, Fitness: {fitness_function(best_individual)}")

    population = new_generation


