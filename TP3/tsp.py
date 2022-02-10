import GeneticAlgorithm as GA
from City import City
import random
import tqdm
import matplotlib.pyplot as plt


# Creating the initial population and then loop through as many generations as we desire.
def genetic_algorithm(population, pop_size, elite_size, mutation_rate, generations):
    pop = GA.initial_population(pop_size, population)
    print(f"Initial distance: {str(1 / GA.rank_routes(pop)[0][1])}")
    initial_route_index = GA.rank_routes(pop)[0][0]
    initial_route = pop[initial_route_index]
    first_element = initial_route[0]
    initial_route.append(first_element)
    plot_route(initial_route, "Initial best route")
    for _ in tqdm.tqdm(range(generations)):
        pop = GA.next_generation(pop, elite_size, mutation_rate)

    print(f"Final distance: {str(1 / GA.rank_routes(pop)[0][1])}")
    best_route_index = GA.rank_routes(pop)[0][0]
    best_route = pop[best_route_index]
    best_route.append(best_route[0])
    return best_route


# To plot the route using matplotlib.
def plot_route(best_route, title):
    annotations = [str(i) for i in range(len(best_route))]
    x = [i.x for i in best_route]
    y = [i.y for i in best_route]
    plt.scatter(x, y, c='red')
    for i, txt in enumerate(annotations):
        plt.annotate(txt, (x[i], y[i]))
    plt.plot(x, y)
    plt.title(title)
    plt.show()


# To run the algorithm.
def run_genetic_algorithm(num_cities, pop_size, elite_size, mutation_rate, generations):
    cities_list = []
    for i in range(num_cities):
        cities_list.append(City(x=int(random.random() * 200), y=int(random.random() * 200)))
    best_route = genetic_algorithm(cities_list, pop_size, elite_size, mutation_rate, generations)
    plot_route(best_route, "Final best route")


# To input a number and make sure that it's really an Int.
def input_number_int(message):
    while True:
        try:
            user_input = int(input(message))
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            return user_input


# To input a float and make sure it's really a Float.
def input_number_float(message):
    while True:
        try:
            user_input = float(input(message))
            if user_input > 1:
                print("The rate needs to be lower than 1! Try again")
            elif user_input < 0:
                print("The rate needs to be higher than 0! Try again")
            else:
                return user_input
        except ValueError:
            print("Not an float! Try again.")
            continue


# To combine the inputs and then run the genetic algorithm.
def inputs_and_runs():
    num_cities = input_number_int("Entrez le nombre de villes souhaité: ")
    pop_size = input_number_int("Entrez la taille de la population souhaitée pour chaque génération: ")
    elite_size = input_number_int("Entrez la taille de l'élite: ")
    mutation_rate = input_number_float("Entrez le taux de mutation: ")
    generations = input_number_int("Entrez le nombre de générations: ")
    run_genetic_algorithm(num_cities, pop_size, elite_size, mutation_rate, generations)


if __name__ == "__main__":
    inputs_and_runs()
