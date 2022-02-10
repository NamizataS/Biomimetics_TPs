import random, operator
import numpy as np
import pandas as pd

from Fitness import Fitness


# Randomly select the order in which we visit each city. Initial route. This produces one individual
def create_route(city_list):
    route = random.sample(city_list, len(city_list))
    return route


# To create a full population.
# Looping through the createRoute function until we have as many routes as we want for our population
def initial_population(pop_size, city_list):
    population = []
    for i in range(0, pop_size):
        population.append(create_route(city_list))
    return population


# Make use of the fitness class to rank each individual in the population.
# The output is an ordered list with the route ID and each associated fitness score.
def rank_routes(population):
    fitness_res = {}
    for i in range(len(population)):
        fitness_res[i] = Fitness(population[i]).route_fitness()
    return sorted(fitness_res.items(), key=operator.itemgetter(1), reverse=True)


# Use the output from rankRoutes to determine which routes to select in our select functions.
# Then set up the roulette wheel by calculating a relative fitness weight for each individual.
# Comparing randomly drawn number to these weights to select our mating pool.
# Returns a list of route ID which we can use to create the mating pool.
def selection(pop_ranked, elite_size):
    selection_res = []
    df = pd.DataFrame(np.array(pop_ranked), columns=["Index", "Fitness"])
    df['tot_sum'] = df.Fitness.cumsum()
    df['tot_perc'] = 100 * df.tot_sum / df.Fitness.sum()

    for i in range(elite_size):
        selection_res.append(pop_ranked[i][0])
    for i in range(len(pop_ranked) - elite_size):
        pick = 100 * random.random()
        for j in range(len(pop_ranked)):
            if pick <= df.iat[j, 3]:
                selection_res.append(pop_ranked[i][0])
                break
    return selection_res


# Simply extracting the selected individuals from our population using the ID's of the routes selected in the selection function
def mating_pool(population, selection_res):
    mating_pool_var = []
    for i in range(len(selection_res)):
        index = selection_res[i]
        mating_pool_var.append(population[index])
    return mating_pool_var


# Create the next generation in a process called crossover.
# We randomly select a subset if the first parent string and then fill the remainder of the route with the genes from
# the second parent in the order in which they appear without duplicating any genes in the selected subset from the first parent.
def breed(parent1, parent2):
    child_par1 = []
    gene_a = int(random.random() * len(parent1))
    gene_b = int(random.random() * len(parent2))

    start_gene = min(gene_a, gene_b)
    end_gene = max(gene_a, gene_b)
    for i in range(start_gene, end_gene):
        child_par1.append(parent1[i])
    child_par2 = [item for item in parent2 if item not in child_par1]
    child = child_par1 + child_par2
    return child


# Generalize the previous function to create our offspring population.
# Use elitism to retain the best routes from the current population then fill out the rest of the next generation.
def breed_population(mating_pool, elite_size):
    children = []
    length = len(mating_pool) - elite_size
    pool = random.sample(mating_pool, len(mating_pool))

    for i in range(elite_size):
        children.append(mating_pool[i])
    for i in range(length):
        child = breed(pool[i], pool[len(mating_pool) - i - 1])
        children.append(child)
    return children


# We can't drop cities, so we'll use swap mutation.
# With specified low probability, two cities will swap places in our route.
def mutate(individual, mutation_rate):
    for swapped in range(len(individual)):
        if random.random() < mutation_rate:
            swap_with = int(random.random() * len(individual))
            city1 = individual[swapped]
            city2 = individual[swap_with]
            individual[swapped] = city2
            individual[swap_with] = city1
    return individual


# We extend the mutate function to our whole population.
def mutate_population(population, mutation_rate):
    mutated_pop = []
    for individual in range(len(population)):
        mutate_ind = mutate(population[individual], mutation_rate)
        mutated_pop.append(mutate_ind)
    return mutated_pop


# Function to produce a new generation.
# First we rank the routes in the current generation using rankRoutes.
# Determine our potential parents by running the selection function which allows us to create the mating pool.
# Finally, we create our new generation using the breedPopulation function and applying mutation using mutatePopulation.
def next_generation(current_gen, elite_size, mutation_rate):
    pop_ranked = rank_routes(current_gen)
    selection_res = selection(pop_ranked, elite_size)
    matingpool = mating_pool(current_gen, selection_res)
    children = breed_population(matingpool, elite_size)
    next_gen = mutate_population(children, mutation_rate)
    return next_gen
