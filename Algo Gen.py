#Algo génétique

class Genetic:
    def __init__ (self, pop_size, mutation_rate, crossover_rate, elitism_count):
        self.pop_size = pop_size
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.elitisme_count = elitism_count

#Creation d'une population

    def init_population(self, length):
        population = population(self.pop_size, length)
        return population
    
    def eval_population(self, population, fitness_func):

        population_fitness = 0
        for 
#Croisement et mutation de la population

