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
        selection_method1=config['selection_method1'],
        selection_method2=config['selection_method2'],
        selection_ratio=config['selection_ratio'],
        crossover_method=config['crossover_method'],
        mutation_method=config['mutation_method'],
        replacement_strategy1=config['replacement_strategy1'],
        replacement_strategy2=config['replacement_strategy2'],
        replacement_ratio=config['replacement_ratio'],
        temperature=config['temperature'],
        puntos_a_distribuir=config['puntos_a_distribuir'],
        time_limit=config['time_limit'],
        personality=config['personality']
        #The last three to be passed as command line arguments??
    )

    # Run the genetic algorithm
    best_solution = ga.run()
    print("Best solution found:", best_solution)

if __name__ == "__main__":
    main()