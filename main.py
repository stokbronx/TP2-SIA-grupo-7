# main.py

import random
from genetic_algorithm import GeneticAlgorithm
from config_reader import load_config


def main():
    # Step 1: Load configuration (we'll define this function in config_reader.py)
    config = load_config('config.json')

    # Step 2: Initialize the Genetic Algorithm with the loaded config
    ga = GeneticAlgorithm(
        population_size=config['population_size'],
        crossover_rate=config['crossover_rate'],
        mutation_rate=config['mutation_rate'],
        max_generations=config['max_generations']
    )

    # Step 3: Run the genetic algorithm
    best_solution = ga.run()

    # Step 4: Print the best solution
    print("Best character found: ", best_solution)


if __name__ == "__main__":
    main()