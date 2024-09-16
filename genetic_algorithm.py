import random
from eve_calc import calculate
class GeneticAlgorithm:
    def __init__(self, population_size, crossover_rate, mutation_rate, max_generations, selection_method, crossover_method, mutation_method, replacement_strategy, puntos_a_distribuir, time_limit, personality):
        self.population_size = population_size
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.max_generations = max_generations
        self.crossover_method = crossover_method
        self.selection_method = selection_method
        self.mutation_method = mutation_method
        self.replacement_strategy = replacement_strategy
        self.puntos_a_distribuir = puntos_a_distribuir
        self.time_limit = time_limit
        self.personality = personality

        self.population = []



    def initialize_population(self):
        # Create initial population (this is just a placeholder)
        for _ in range(self.population_size):
            # Each individual could be a list of attributes for the character
            individual = self.create_random_individual()
            self.population.append(individual)

    def create_random_individual(self):
        puntos_a_distribuir = self.puntos_a_distribuir
        # Define a random individual (for now, just random numbers as placeholders)
        random_numbers = [random.randint(1, 100) for _ in range(5)]
        total = sum(random_numbers)
        normalized_numbers = [num / total for num in random_numbers]
        return {
            'height': random.uniform(1.3, 2.0),
            'strength': normalized_numbers[0] * puntos_a_distribuir,
            'dexterity': normalized_numbers[1] * puntos_a_distribuir,
            'intelligence': normalized_numbers[2] * puntos_a_distribuir,
            'vigor': normalized_numbers[3] * puntos_a_distribuir,
            'constitution': normalized_numbers[4] * puntos_a_distribuir
        }

    def run(self):
        # Main loop of the genetic algorithm
        self.initialize_population()

        for generation in range(self.max_generations):
            # For now, let's just print the generation number
            print(f"Generation {generation}")

            # Evaluate fitness for each individual
            self.evaluate_population()

            # Select parents for crossover (placeholder for now)
            parents = self.select_parents()

            # Perform crossover and mutation to create the next generation (we'll add this logic later)
            self.population = self.create_next_generation(parents)

        # For now, just return the best individual (later, this will be based on fitness)
        return self.population[0]


    def evaluate_population(self):
        for individual in self.population:
            individual['fitness'] = calculate(individual['personality'], individual['strength'], individual['dexterity'], individual['intelligence'], individual['vigor'], individual['constitution'], individual['height']   )

        print("Evaluating population...")

    def select_parents(self):
        # Placeholder: This function will select individuals for crossover
        print("Selecting parents...")
        if self.selection_method == "elite":
            return self.elite_selection()
        return self.population[:2]  # Just select the first two individuals for now

    def create_next_generation(self, parents):
        # Placeholder: This function will generate the next generation by crossover and mutation
        print("Creating next generation...")
        return parents  # For now, just return the parents as the next generation