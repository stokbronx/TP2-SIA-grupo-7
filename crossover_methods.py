def single_point_crossover(parents):
    children = []
    while len(parents) >= 2:
        # Select two parents randomly
        parent1, parent2 = random.sample(parents, 2)
        # Remove the selected parents from the pool
        parents.remove(parent1)
        parents.remove(parent2)
        # Select a random crossover point
        crossover_point = random.randint(1, len(parent1) - 1)
        # Perform crossover
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point] + parent1[crossover_point:]
        # Add children to the list
        children.append(child1)
        children.append(child2)
    return children