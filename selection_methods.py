import random
#methods for selecting the best individuals from the population

def elite_selection(population, num_elites):
    # Sort the population by fitness
    population.sort(key=lambda x: x['fitness'], reverse=True)
    # Return the top 'num_elites' individuals
    return population[:num_elites]

def roulette_selection(population, num_parents):
    # Calculate total fitness of the population
    total_fitness = sum([individual['fitness'] for individual in population])
    # Calculate selection probabilities for each individual
    selection_probs = [individual['fitness'] / total_fitness for individual in population]
    # Select parents based on the selection probabilities
    parents = random.choices(population, weights=selection_probs, k=num_parents)
    return parents

def universal_selection(population, num_parents):
    # Calculate total fitness of the population
    total_fitness = sum([individual['fitness'] for individual in population])
    # Calculate selection probabilities for each individual
    selection_probs = [individual['fitness'] / total_fitness for individual in population]
    # Calculate the cumulative probabilities
    cumulative_probs = np.cumsum(selection_probs)
    # Generate random starting point for selection
    start_point = random.uniform(0, 1 / num_parents)
    # Select parents based on the cumulative probabilities
    parents = []
    for i in range(num_parents):
        point = (start_point + i / num_parents) % 1
        for j, prob in enumerate(cumulative_probs):
            if point < prob:
                parents.append(population[j])
                break
    return parents

def boltzmann_selection(population, num_parents, temperature):
    # Calculate selection probabilities based on Boltzmann distribution
    selection_probs = [np.exp(individual['fitness'] / temperature) for individual in population]
    # Normalize the probabilities
    total_prob = sum(selection_probs)
    selection_probs = [prob / total_prob for prob in selection_probs]
    # Select parents based on the selection probabilities
    parents = random.choices(population, weights=selection_probs, k=num_parents)
    return parents

def tournament_selection(population, num_parents):
    tournament_size = int(len(population)/2)
    parents = []
    for _ in range(num_parents):
        # Randomly select 'tournament_size' individuals from the population
        tournament = random.sample(population, tournament_size)
        # Select the best individual from the tournament
        winner = max(tournament, key=lambda x: x['fitness'])
        parents.append(winner)
    return parents

