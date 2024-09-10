# main.py
from genetic_algorithm import GeneticAlgorithm
from config_reader import load_config

def main():
    # Load hyperparameters from config.json
    config = load_config('config.json')

    # Initialize genetic algorithm with hyperparameters
    ga = GeneticAlgorithm(
        population_size=config['population_size'],
        crossover_rate=config['crossover_rate'],
        mutation_rate=config['mutation_rate'],
        max_generations=config['max_generations'],
        selection_method=config['selection_method'],
        crossover_method=config['crossover_method'],
        mutation_method=config['mutation_method'],
        replacement_strategy=config['replacement_strategy']
    )

    # Run the genetic algorithm
    best_solution = ga.run()
    print("Best solution found:", best_solution)

if __name__ == "__main__":
    main()