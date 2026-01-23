import numpy as np
import matplotlib.pyplot as plt
# C is total time, g : gree time, x:sat(trafic demand),c:cap
def fitness_function(C, g, x, c):
    a = (1 - (g / C)) ** 2 #red light time as fraction pow 2
    # So even though green existed:It didn’t really help. p measures that
    # How much of this green time is actually useful?”
    p = 1 - ((g / C) * x) # how much effectivenes is left- how large effecti required
    # The same red time causes more delay when green is ineffective
    d1 = (0.38 * C * a) / p # delay inver prop to p 

    a2 = 173 * (x ** 2)
    ri1 = np.sqrt((x - 1) + (x - 1) ** 2 + ((16 * x) / c))

    d2= a2 * ri1

    return d1 + d2  # red sign+ congestion(evn green not cleard)

def initialize_population(pop_size, num_lights, green_min, green_max, cycle_time, cars):
    population = []
    road_capacity = [20] * num_lights
    road_congestion = np.array(road_capacity) - np.array(cars)
    road_congestion = road_congestion / np.array(road_capacity)

    while len(population) < pop_size:
        green_times = np.random.randint(green_min, green_max + 1, num_lights)
        if np.sum(green_times) <= cycle_time:
            total_delay = np.sum([fitness_function(cycle_time, green_times[i], road_congestion[i], road_capacity[i]) for i in range(num_lights)])
            population.append((green_times, total_delay))
    return sorted(population, key=lambda x: x[1]) #Sort individuals by tot delay each x based on delay

def roulette_wheel_selection(population, total_delays, beta):
    worst_delay = max(total_delays)
    probabilities = np.exp(-beta * np.array(total_delays) / worst_delay)
    probabilities /= np.sum(probabilities)
    return np.random.choice(len(population), p=probabilities)

def crossover(parent1, parent2, num_lights):
    point = np.random.randint(1, num_lights)
    child1 = np.concatenate([parent1[:point], parent2[point:]])
    child2 = np.concatenate([parent2[:point], parent1[point:]])
    return child1, child2

def mutate(individual, mutation_rate, green_min, green_max):
    num_lights = len(individual)
    mutated = individual.copy()
    for _ in range(int(mutation_rate * num_lights)):
        idx = np.random.randint(0, num_lights)
        sigma = np.random.choice([-1, 1]) * 0.02 * (green_max - green_min)
        mutated[idx] = np.clip(individual[idx] + sigma, green_min, green_max)
    return mutated

def inversion(individual, num_lights):
    idx1, idx2 = np.random.randint(0, num_lights, 2)
    if idx1 > idx2:
        idx1, idx2 = idx2, idx1
    individual[idx1:idx2+1] = individual[idx1:idx2+1][::-1] # reverse sub array
    return individual

def genetic_algorithm(pop_size, num_lights, max_iter, green_min, green_max, cycle_time, mutation_rate, pinv, beta, cars):
    population = initialize_population(pop_size, num_lights, green_min, green_max, cycle_time, cars)
    best_sol = population[0]
    best_delays = [best_sol[1]] # sorted right choosing lowest delay

    road_capacity = [20] * num_lights
    road_congestion = np.array(road_capacity) - np.array(cars)
    road_congestion = road_congestion / np.array(road_capacity)

    for _ in range(max_iter):
        total_delays = [ind[1] for ind in population]
        new_population = []
# Premature Convergence :
# Premature convergence means the Genetic Algorithm settles on a solution too early and stops improving, even though better solutions exist.roulet wheel solves this
        MAX_ATTEMPTS = pop_size * 10
        attempts = 0
        while len(new_population) < pop_size and attempts < MAX_ATTEMPTS:
            attempts += 1
            i1 = roulette_wheel_selection(population, total_delays, beta)
            i2 = roulette_wheel_selection(population, total_delays, beta)

            parent1, parent2 = population[i1][0], population[i2][0]
            child1, child2 = crossover(parent1, parent2, num_lights) # taking good parts from 2

            if np.sum(child1) <= cycle_time:
                child1 = mutate(child1, mutation_rate, green_min, green_max)
                child1 = np.clip(child1, green_min, green_max)
                total_delay = np.sum([fitness_function(cycle_time, child1[i], road_congestion[i], road_capacity[i]) for i in range(num_lights)])
                new_population.append((child1, total_delay))

            if np.sum(child2) <= cycle_time:
                child2 = mutate(child2, mutation_rate, green_min, green_max)
                child2 = np.clip(child2, green_min, green_max)
                total_delay = np.sum([fitness_function(cycle_time, child2[i], road_congestion[i], road_capacity[i]) for i in range(num_lights)])
                new_population.append((child2, total_delay))
        # enitre new genaration new 400 genrated else using inversion comple 400
        # Apply inversion
        while len(new_population) < pop_size:
            i = np.random.randint(0, len(population))
            individual = inversion(population[i][0], num_lights)
            if np.sum(individual) <= cycle_time:
                individual = mutate(individual, mutation_rate, green_min, green_max)
                total_delay = np.sum([fitness_function(cycle_time, individual[i], road_congestion[i], road_capacity[i]) for i in range(num_lights)])
                new_population.append((individual, total_delay))

        # Merge and select the best population
        population += new_population
        population = sorted(population, key=lambda x: x[1])[:pop_size]
        
        if population[0][1] < best_sol[1]: # foud lesser delay make it as best sol,
            best_sol = population[0]
        
        best_delays.append(best_sol[1])
        print(f"Iteration: Best Total Delay = {best_sol[1]}")
        print(f"Green Times: North = {best_sol[0][0]}, South = {best_sol[0][1]}, West = {best_sol[0][2]}, East = {best_sol[0][3]}")
    
    return best_sol, best_delays

def optimize_traffic(cars):
    # Default parameters
    pop_size = 400
    num_lights = 4
    max_iter = 25 # re genrations
    green_min = 10
    green_max = 60
    cycle_time = 160 - 12 # avg grren/cycle + yellw change minus
    mutation_rate = 0.02 # cross parent
    pinv = 0.2 #order changeing(size=4)(prob of inversion)rev rand subary
    beta = 8 # how congestion is penalised
    #how harshly GA reacts to traffic imbalance.

    # Run Genetic Algorithm with default parameters
    best_sol, best_delays = genetic_algorithm(pop_size, num_lights, max_iter, green_min, green_max, cycle_time, mutation_rate, pinv, beta, cars)

    # Convert numpy types to standard Python types
    result = {
        'north': int(best_sol[0][0]),
        'south': int(best_sol[0][1]),
        'west': int(best_sol[0][2]),
        'east': int(best_sol[0][3])
    }

    print('Optimal Solution:')
    print(f'North Green Time = {result["north"]} seconds')
    print(f'South Green Time = {result["south"]} seconds')
    print(f'West Green Time = {result["west"]} seconds')
    print(f'East Green Time = {result["east"]} seconds')
    # print(best_delays) # sum of 4 lanes dealay vector
    print([f"{x:.3f}" for x in best_delays])

    return result
