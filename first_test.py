import random

# Step 1: Initialization
def initialize_population(population_size, x_range):
    population = []
    for _ in range(population_size):
        x_value = random.uniform(x_range[0], x_range[1])
        population.append([x_value])
    return population

# Step 2: Fitness Function
def fitness_function(chromosome):
    return -chromosome[0] ** 2

# Step 3: Selection
def parent_selection(population, fitness_function, tournament_size):
    selected_parents = []
    for _ in range(len(population)):
        tournament = random.sample(population, tournament_size)
        winner = max(tournament, key=fitness_function)
        selected_parents.append(winner)
    return selected_parents

# Step 4: Crossover (Single-Point Crossover)
def single_point_crossover(parent1, parent2):
    if isinstance(parent1[0], list):
        crossover_point = random.randint(0, len(parent1[0]) - 1)
        child1 = parent1[0][:crossover_point] + parent2[0][crossover_point:]
        child2 = parent2[0][:crossover_point] + parent1[0][crossover_point:]
        return [child1], [child2]
    else:
        crossover_point = random.random()
        child1 = crossover_point * parent1[0] + (1 - crossover_point) * parent2[0]
        child2 = crossover_point * parent2[0] + (1 - crossover_point) * parent1[0]
        return [child1], [child2]

# Step 5: Mutation
def mutation(child, mutation_rate, x_range):
    if random.random() < mutation_rate:
        mutation_amount = random.uniform(-0.5, 0.5)
        child[0] += mutation_amount
        child[0] = max(x_range[0], min(x_range[1], child[0]))
    return child

# Step 6: Genetic Algorithm
def genetic_algorithm(fitness_function, x_range, population_size, generations, tournament_size, mutation_rate):
    population = initialize_population(population_size, x_range)

    for generation in range(generations):
        # Evaluate fitness for each individual in the population
        fitness_scores = [fitness_function(x) for x in population]

        # Select parents using tournament selection
        parents = parent_selection(population, fitness_function, tournament_size)

        # Perform crossover to create offspring
        offspring = []
        for i in range(0, len(parents), 2):
            parent1 = parents[i]
            parent2 = parents[i + 1]
            child1, child2 = single_point_crossover(parent1, parent2)
            offspring.extend([child1, child2])

        # Apply mutation to the offspring
        offspring = [mutation(child, mutation_rate, x_range) for child in offspring]

        # Replace the old population with the combined population of parents and offspring
        population = parents + offspring

    # Return the best solution found
    best_solution = max(population, key=fitness_function)
    return best_solution

# Testing
population_size = 4
generations = 10
tournament_size = 2
mutation_rate = 0.1
x_range = (-10, 10)

best_solution = genetic_algorithm(fitness_function, x_range, population_size, generations, tournament_size, mutation_rate)

print("Best solution:", best_solution[0])
print("Best fitness:", fitness_function(best_solution))
