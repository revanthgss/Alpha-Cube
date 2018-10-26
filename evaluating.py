import numpy as np
import cmath

city = np.array([(5,2,4,8,9,0,3,3,8,7),(5,5,3,4,4,6,4,1,9,1),(4,1,2,1,3,8,7,8,9,1),(1,7,1,6,9,3,1,9,6,9),(4,7,4,9,9,8,6,5,4,2),(7,5,8,2,5,2,3,9,8,2),(1,4,0,6,8,4,0,1,2,1),(1,5,2,1,2,8,3,3,6,2),(4,5,9,6,3,9,7,6,5,10),(0,6,2,8,7,1,2,1,5,3)])
population = np.random.permutation(10)

def distance_of(non_proposed, proposed, fire_freq):
    n = non_proposed;
    fs = proposed;

    sizen = np.argwhere(city==n)
    sizes = np.argwhere(city==fs)
    xn = sizen[0,0]
    yn = sizen[0,1]

    xs = sizes[0,0]
    ys = sizes[0,1]
    
    w = fire_freq;

    distance_ = w * cmath.sqrt( (xn-xs)^2 + (yn-ys)^2 )
    return distance_

def cost_of(proposed):
    cost_ = 0;
    size=np.size(city)-1
    for pos in range(0,size):
             if (pos != proposed):
                  non_proposed = pos;
                  fire_freq = city[pos];
                  cost_ = cost_ + distance_of(non_proposed, proposed, fire_freq) 
                  return cost_


def response_time_of(fire_station):
    r = cost_of(fire_station)
    time = 1.7 + 3.4 * r
    return time

def truncation_selection(population, proportion):
	
    
    population_size = np.size(population)

    ##cell_population = num2cell(population)

    ## %%sort population cell array by fitness cost
    ##[~,sorted_fitnesses] = sort(cellfun(@(loc)cost_of(loc),cell_population))
    
    population = population[sorted_fitnesses]
    N = population_size * proportion;
    parents = population[1:N]
    return parents,N


def crossover(parents, population, N):
	
    children_ = []
    for parent_ in range(1,np.size(parents),2):
                
                parent1 = parents[parent_]
                parent2 = parents[parent_ + 1]

                size1 = np.argwhere(city==parent1)
                size2 = np.argwhere(city==parent2)
                
                x1 = size1[0,0]
                y1 = size1[0,1]

                x2 = size2[0,0]
                y2 = size2[0,1]

                child = numpy.zeros(1, 2)

                if (np.random.randint(2,1) == 1):
                        child[1] = x1;
                else:
                        child[1] = y1;
                    

                if (np.random.randint(2,1) == 1):
                        child[2] = x2;
                else:
                        child[2] = y2;
                    

                xc = child[1]
                yc = child[2]
                
                location = xc*10+yc;

            
                children_ = np.append(children_,location)
	
    children = np.asarray(children_)
    return children


def mutate(children_, mutation_rate, parents, population, N):
    	
	new_population = []
	population_size = np.size(population)
	N = N/2

	for child in range(1,np.size(children_)):
		if (np.random.rand(1)[0] < mutation_rate):
                        sizec = np.argwhere(city==children_[child])
			xc = sizec[0]
			yc = sizec[1]
			mutated = xc*10+yc
			children_[child] = mutated
		
	
	new_population = np.append(children_,np.append(parents,population(N+1:population_size)))

	#cell_new_population = num2cell(new_population)
        #[~,sorted_fitnesses] = sort(cellfun(@(loc)cost_of(loc),cell_new_population))
	
        new_population = new_population[sorted_fitnesses]
        new_population = new_population[1:population_size-1]
    
        return new_population
    

init_value = population[0]
gens = np.array([0])

pos = np.argwhere(city==10)
x = pos[0,0]
y = pos[0,1]

costs = cost_of(init_value)

print(np.size(costs))
