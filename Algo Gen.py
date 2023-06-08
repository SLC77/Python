# ### Etape 2
# ## Calcul population

# import random

# # Paramètres de l'algorithme génétique
# taille_population = 20
# taille_individu = 8
# taux_mutation = 0.1
# nombre_iterations = 1500

# # Fonction d'évaluation (fonction objectif)
# def evaluer_individu(individu):
#     # Ici, nous utilisons une fonction d'évaluation simple qui compte le nombre de '1' dans l'individu
#     return individu.count('1')

# # Fonction de création d'un individu aléatoire
# def creer_individu():
#     return ''.join(random.choice(['0', '1']) for _ in range(taille_individu))

# # Fonction de création d'une population initiale
# def creer_population():
#     return [creer_individu() for _ in range(taille_population)]

# # Fonction de croisement (crossover)
# def croiser(parent1, parent2):
#     point_croisement = random.randint(1, taille_individu - 1)
#     enfant1 = parent1[:point_croisement] + parent2[point_croisement:]
#     enfant2 = parent2[:point_croisement] + parent1[point_croisement:]
#     return enfant1, enfant2

# # Fonction de mutation
# def muter(individu):
#     indice_mutation = random.randint(0, taille_individu - 1)
#     liste_individu = list(individu)
#     liste_individu[indice_mutation] = '0' if liste_individu[indice_mutation] == '1' else '1'
#     return ''.join(liste_individu)

# # Fonction principale de l'algorithme génétique
# def algorithme_genetique():
#     population = creer_population()
    
#     for iteration in range(nombre_iterations):
#         # Évaluation de la population
#         scores = [evaluer_individu(individu) for individu in population]
        
#         # Sélection des parents (roulette wheel selection)
#         somme_scores = sum(scores)
#         probas_selection = [score / somme_scores for score in scores]
#         parents = random.choices(population, weights=probas_selection, k=2)
        
#         # Croisement des parents pour créer de nouveaux individus
#         enfant1, enfant2 = croiser(parents[0], parents[1])
        
#         # Mutation des nouveaux individus
#         if random.random() < taux_mutation:
#             enfant1 = muter(enfant1)
#         if random.random() < taux_mutation:
#             enfant2 = muter(enfant2)
        
#         # Remplacement de certains individus de la population par les nouveaux individus
#         index_remplacement = random.randint(0, taille_population - 1)
#         population[index_remplacement] = enfant1
#         index_remplacement = random.randint(0, taille_population - 1)
#         population[index_remplacement] = enfant2
    
#     # Sélection du meilleur individu de la population finale
#     meilleur_individu = max(population, key=evaluer_individu)
#     meilleur_score = evaluer_individu(meilleur_individu)
    
#     return meilleur_individu, meilleur_score

# # Exécution de l'algorithme génétique
# meilleur_individu, meilleur_score = algorithme_genetique()

# # Affichage du résultat
# print("Meilleur individu trouvé :", meilleur_individu)
# print("Meilleur score trouvé :", meilleur_score)

class GeneticAlgorithm:
    def __init__(self, population_size, mutation_rate, crossover_rate, elitism_count):
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.elitism_count = elitism_count

    def init_population(self, chromosome_length):
        # Initialisation de la population
        population = Population(self.population_size, chromosome_length)
        return population

    def eval_population(self, population, fitness_func):
        # Évaluation de la population
        population_fitness = 0
        for individual in population.get_individuals():
            individual_fitness = fitness_func(individual)
            individual.set_fitness(individual_fitness)
            population_fitness += individual_fitness
        population.set_population_fitness(population_fitness)

    def select_parent(self, population):
        # Sélection des parents
        individuals = population.get_individuals()
        roulette_wheel_position = random.random() * population.get_population_fitness()
        spin_wheel = 0
        for individual in individuals:
            spin_wheel += individual.get_fitness()
            if spin_wheel >= roulette_wheel_position:
                return individual
        return individuals[-1]

    def crossover_population(self, population):
        # Croisement de la population
        new_population = Population(population.size())
        for pop_idx in range(population.size()):
            parent1 = population.get_fittest(pop_idx)
            if self.crossover_rate > random.random() and pop_idx >= self.elitism_count:
                offspring = Individual(parent1.chromosome_length())
                parent2 = self.select_parent(population)
                for gene_idx in range(parent1.chromosome_length()):
                    if random.random() > 0.5:
                        offspring.set_gene(gene_idx, parent1.get_gene(gene_idx))
                    else:
                        offspring.set_gene(gene_idx, parent2.get_gene(gene_idx))
                new_population.set_individual(pop_idx, offspring)
            else:
                new_population.set_individual(pop_idx, parent1)
        return new_population

    def mutate_population(self, population):
        # Mutation de la population
        new_population = Population(population.size())
        for pop_idx in range(population.size()):
            individual = population.get_fittest(pop_idx)
            if pop_idx >= self.elitism_count:
                for gene_idx in range(individual.chromosome_length()):
                    if self.mutation_rate > random.random():
                        new_gene = 1 if random.random() > 0.5 else 0
                        individual.set_gene(gene_idx, new_gene)
            new_population.set_individual(pop_idx, individual)
        return new_population

    def run(self, fitness_func, chromosome_length, max_generations):
        # Exécution de l'algorithme génétique
        population = self.init_population(chromosome_length)
        self.eval_population(population, fitness_func)
        generation = 1
        while generation < max_generations:
            population = self.crossover_population(population)
            population = self.mutate_population(population)
            self.eval_population(population, fitness_func)
            generation += 1
        return population.get_fittest(0)

class Individual:
    def __init__(self, chromosome_length):
        self._chromosome = [random.randint(0, 1) for _ in range(chromosome_length)]
        self._fitness = -1

    def get_chromosome(self):
        return self._chromosome

    def get_gene(self, offset):
        return self._chromosome[offset]

    def set_gene(self, offset, gene):
        self._chromosome[offset] = gene

    def get_fitness(self):
        return self._fitness

    def set_fitness(self, fitness):
        self._fitness = fitness

    def chromosome_length(self):
        return len(self._chromosome)

class Population:
    def __init__(self, population_size, chromosome_length=None):
        self._individuals = []
        
        if chromosome_length is not None:
            for _ in range(population_size):
                individual = Individual(chromosome_length)
                self._individuals.append(individual)

    def get_individuals(self):
        return self._individuals

    def set_individual(self, offset, individual):
        self._individuals[offset] = individual

    def get_fittest(self, offset):
        sorted_individuals = sorted(self._individuals,
                                    key=lambda x: x.get_fitness(),
                                    reverse=True)
        print(sorted_individuals)
        
