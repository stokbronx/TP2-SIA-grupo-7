import random #just a test!
import matplotlib.pyplot as plt
import numpy as np

from eve_calc import calculate

class MutationAlgorithm:
    def __init__(self, population_size, mutation_rate, mutation_method):
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.mutation_method = mutation_method
        self.population = []

    def initialize_population(self):
        # Create initial population
        for _ in range(self.population_size):
            individual = self.create_random_individual()
            self.population.append(individual)

    def create_random_individual(self):
        # Define a random individual
        return {
            'height': random.uniform(1.3, 2.0),
            'strength': random.randint(10, 50),
            'dexterity': random.randint(10, 50),
            'intelligence': random.randint(10, 50),
            'vigor': random.randint(10, 50),
            'constitution': random.randint(10, 50)
        }

    def mutate_population(self):
        # Apply mutation to each individual in the population
        for individual in self.population:
            if random.random() < self.mutation_rate:
                self.mutation_method(individual)

# Example mutation method
def example_mutation_method(individual):
    # Mutate the individual's attributes
    individual['strength'] += random.randint(-5, 5)
    individual['dexterity'] += random.randint(-5, 5)
    individual['intelligence'] += random.randint(-5, 5)
    individual['vigor'] += random.randint(-5, 5)
    individual['constitution'] += random.randint(-5, 5)

# Usage
mutation_algorithm = MutationAlgorithm(
    population_size=10,
    mutation_rate=0.1,
    mutation_method=example_mutation_method
)

mutation_algorithm.initialize_population()

initial_attributes = {
    'strength': [ind['strength'] for ind in mutation_algorithm.population],
    'dexterity': [ind['dexterity'] for ind in mutation_algorithm.population],
    'intelligence': [ind['intelligence'] for ind in mutation_algorithm.population],
    'vigor': [ind['vigor'] for ind in mutation_algorithm.population],
    'constitution': [ind['constitution'] for ind in mutation_algorithm.population]
}

mutation_algorithm.mutate_population()

mutated_attributes = {
    'strength': [ind['strength'] for ind in mutation_algorithm.population],
    'dexterity': [ind['dexterity'] for ind in mutation_algorithm.population],
    'intelligence': [ind['intelligence'] for ind in mutation_algorithm.population],
    'vigor': [ind['vigor'] for ind in mutation_algorithm.population],
    'constitution': [ind['constitution'] for ind in mutation_algorithm.population]
}

fig, axs = plt.subplots(5, 1, figsize=(10, 20))

attributes = ['strength', 'dexterity', 'intelligence', 'vigor', 'constitution']
for i, attr in enumerate(attributes):
    axs[i].plot(initial_attributes[attr], 'bo-', label='Initial')
    axs[i].plot(mutated_attributes[attr], 'ro-', label='Mutated')
    axs[i].set_title(attr.capitalize())
    axs[i].legend()

plt.tight_layout()
plt.show()

