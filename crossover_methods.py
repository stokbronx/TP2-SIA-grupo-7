import random

def single_point_crossover(parents):
    children = []
    while len(parents) >= 2:
        # Select two parents randomly
        parent1, parent2 = random.sample(parents, 2)
        # Remove the selected parents from the pool
        parents.remove(parent1)
        parents.remove(parent2)
        # Select a random crossover point
        crossover_point = random.randint(0, len(parent1) - 1)
        # Perform crossover
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point] + parent1[crossover_point:]
        # Add children to the list
        children.append(child1)
        children.append(child2)
    return children


def double_point_crossover(parents):
    children = []
    while len(parents) >= 2:
        #Select 2 parents
        parent1, parent2 = random.sample(parents,2)
        #Remove parents from available pool
        parents.remove(parent1)
        parents.remove(parent2)
        #Select Crossover points
        cross_pt1 = random.randint(0, len(parent1) - 1)
        cross_pt2 = random.randint(0, len(parent1) - 1)
        #Find max and min crossover point
        mincross_pt = min(cross_pt1, cross_pt2)
        maxcross_pt = max(cross_pt1, cross_pt2)
        #Do de crossover
        child1 = parent1[:mincross_pt] + parent2[mincross_pt:maxcross_pt] + parent1[maxcross_pt:]
        child2 = parent2[:mincross_pt] + parent1[mincross_pt:maxcross_pt] + parent2[maxcross_pt:]
        #Add children to list
        children.append(child1)
        children.append(child2)
    return children

def anular_crossover(parents):
    children = []
    while len(parents) >= 2:
        #Select 2 parents
        parent1, parent2 = random.sample(parents,2)
        #Remove parents from available pool
        parents.remove(parent1)
        parents.remove(parent2)
        #Select crossover point and lenght
        crossover_pt = random.randint(0, len(parent1) - 1)
        length_cross = random.randint(0, len(parent1)//2)
        genome_length = len(parent1)
        # Create offspring as copies of the parents
        offspring1 = parent1[:]
        offspring2 = parent2[:]

        # Perform crossover in the circular portion
        for i in range(length_cross):
            index = (crossover_pt + i) % genome_length  # This allows wrapping around the genome
            offspring1[index], offspring2[index] = offspring2[index], offspring1[index]  # Swap genes
            
        children.append(offspring1)
        children.append(offspring2)
        
    return children


def uniform_crossover(parents):
    children = []
    while len(parents) >= 2:
        #Select 2 parents
        parent1, parent2 = random.sample(parents,2)
        #Remove parents from available pool
        parents.remove(parent1)
        parents.remove(parent2)
        
        child1 = parent1[:]
        child2 = parent2[:]
        
        for i in range(len(parent1)):
            cutoff = random.randrange(0,1) 
            if cutoff > 0.5:
                child1[i] = parent1[i]
                child2[i] = parent2[i]
            else:
                child1[i] = parent2[i]
                child2[i] = parent1[i]
                
        children.append(child1)
        children.append(child2)
        
    return children
