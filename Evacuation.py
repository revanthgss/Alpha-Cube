global city
city = load_locations()


population = init_population(100)
init_value = population(1)

gens = mcat([0])
costs = mcat([cost_of(init_value)])
[x, y] = coord_of(init_value)
coords = mcat([sprintf(mstring('(%d, %d)'), x, y)])
time = mcellarray([sprintf(mstring('%f min'), response_time_of(init_value))])
xs = mcat([x])
ys = mcat([y])

fprintf(mstring('INITIAL COORDS: (%d, %d)\\n'), x, y)
fprintf(mstring('INITIAL COST: %f\\n['), cost_of(population(1)))

for generation in mslice[1:100]:
    [parents, N] = truncation_selection(population, 0.50)
    children_ = crossover(parents, population, N)
    population = mutate(children_, 0.2, parents, population, N)

    loc_of_best = population(1)
    freq_of_best = city(loc_of_best)
    cost_of_best = cost_of(loc_of_best)
    [x, y] = coord_of(loc_of_best)
    response_time_of_best = response_time_of(loc_of_best)

    #fprintf('gen: %d [%d %d]: %f %f\n', generation, x, y, cost_of_best, response_time_of_best)
    fprintf(mstring('='))

    gens = mcat([gens, OMPCSEMI, generation])
    costs = mcat([costs, OMPCSEMI, cost_of_best])
    coords = mcat([coords, OMPCSEMI, sprintf(mstring('(%d, %d)'), x, y)])
    time = mcat([time, OMPCSEMI, sprintf(mstring('%f min'), response_time_of_best)])

    xs = mcat([xs, OMPCSEMI, x])
    ys = mcat([ys, OMPCSEMI, y])

    grid(mstring('on'))
    hold(mstring('on'))
    subplot(2, 1, 1)
    scatter(xs, ys, mstring('filled'))
    axis(mcat([0, 10, 0, 10]))
    set(gca, mstring('XTick'), mcat([mslice[0:10]]))
    set(gca, mstring('YTick'), mcat([mslice[0:10]]))


    grid(mstring('on'))
    hold(mstring('on'))
    subplot(2, 1, 2)

    scatter(gens, costs, mstring('filled'))
    plot(gens, costs, mstring('r'))
    xlabel(mstring('Generations'))
    ylabel(mstring('Cost Value'))
    title(mstring('Cost Value Per Generation (100 Generations)'))
    drawnow()
end

fprintf(mstring(']'))
table(gens, coords, costs, time, mstring('VariableNames'), mcellarray([mstring('Generations'), mstring('ProposedCoordinates'), mstring('CostValue'), mstring('ResponseTime')]))


end




5
(mstring('2'), mstring('4'), mstring('8'), mstring('9'), mstring('0'), mstring('3'), mstring('3'), mstring('8'), mstring('7'))
5
(mstring('5'), mstring('3'), mstring('4'), mstring('4'), mstring('6'), mstring('4'), mstring('1'), mstring('9'), mstring('1'))
4
(mstring('1'), mstring('2'), mstring('1'), mstring('3'), mstring('8'), mstring('7'), mstring('8'), mstring('9'), mstring('1'))
1
(mstring('7'), mstring('1'), mstring('6'), mstring('9'), mstring('3'), mstring('1'), mstring('9'), mstring('6'), mstring('9'))
4
(mstring('7'), mstring('4'), mstring('9'), mstring('9'), mstring('8'), mstring('6'), mstring('5'), mstring('4'), mstring('2'))
7
(mstring('5'), mstring('8'), mstring('2'), mstring('5'), mstring('2'), mstring('3'), mstring('9'), mstring('8'), mstring('2'))
1
(mstring('4'), mstring('0'), mstring('6'), mstring('8'), mstring('4'), mstring('0'), mstring('1'), mstring('2'), mstring('1'))
1
(mstring('5'), mstring('2'), mstring('1'), mstring('2'), mstring('8'), mstring('3'), mstring('3'), mstring('6'), mstring('2'))
4
(mstring('5'), mstring('9'), mstring('6'), mstring('3'), mstring('9'), mstring('7'), mstring('6'), mstring('5'), mstring('10'))
0
(mstring('6'), mstring('2'), mstring('8'), mstring('7'), mstring('1'), mstring('2'), mstring('1'), mstring('5'), mstring('3'))

end

coord_of(pos)
#global city
[x, y] = ind2sub(size(city), pos)
end

@mfunction("time")
def response_time_of(fire_station=None):
    r = cost_of(fire_station)
    time = 1.7 + 3.4 * r
end

@mfunction("cost_")
def cost_of(proposed=None):
 #   global city

    cost_ = 0

    for pos in mslice[1:numel(city)]:
        if pos != proposed:
            #pos
            non_proposed = pos
            fire_freq = city(pos)
            cost_ = cost_ + distance_of(non_proposed, proposed, fire_freq)
            # else
            #   pos
            #   city(pos)
        end
    end
end

@mfunction("distance_")
def distance_of(non_proposed=None, proposed=None, fire_freq=None):
    n = non_proposed
    fs = proposed

    [xn, yn] = coord_of(n)
    [xfs, yfs] = coord_of(fs)
    w = fire_freq

    distance_ = w * sqrt((xn - xfs) ** 2 + (yn - yfs) ** 2)
end

@mfunction("population")
def init_population(population_size=None):
    #global city
    # for each new chromosome of population,
    #   generate a random location order
    population = randperm(100)
end

truncation_selection(population, proportion)

#global city
population_size = length(population)

# put population matrix to population cell array
cell_population = num2cell(population)

# sort population cell array by fitness cost
sort(cellfun(lambda loc: cost_of(loc), cell_population))
population = population(sorted_fitnesses)


# get N-best fitnesses based on proportion
N = population_size * proportion

# set N-best fitnesses as parents
parents = population(mslice[1:N])
end

@mfunction("children_")
def crossover(parents=None, population=None, N=None):
 #   global city
    children_ = mcat([])

    for parent_ in mslice[1:2:length(parents)]:
        # CROSSOVER
        parent1 = parents(parent_)
        parent2 = parents(parent_ + 1)

        [x1, y1] = coord_of(parent1)
        [x2, y2] = coord_of(parent2)

        child = zeros(1, 2)

        if randi(2) == 1:
            child(1).lvalue = x1
        else:
            child(1).lvalue = y1
        end

        if randi(2) == 1:
            child(2).lvalue = x2
        else:
            child(2).lvalue = y2
        end

        xc = child(1)
        yc = child(2)
        location = sub2ind(size(city), xc, yc)

        #fprintf('%d %d\n', city(child(1), child(2)), city(location))

        children_ = mcat([children_, location])
    end
    #children_
end

@mfunction("new_population")
def mutate(children_=None, mutation_rate=None, parents=None, population=None, N=None):
  #  global city

    new_population = mcat([])
    population_size = length(population)
    N = N / 2

    for child in mslice[1:length(children_)]:
        if rand(1) < mutation_rate:
            [xc, yc] = coord_of(children_(child))
            mutated = sub2ind(size(city), yc, xc)
            children_(child).lvalue = mutated
        end
    end
    #children_
    #population( N+1:population_size )

    new_population = mcat([children_, parents, population(mslice[N + 1:population_size])])

    cell_new_population = num2cell(new_population)

    # sort population cell array by fitness cost
    sort(cellfun(lambda loc: cost_of(loc), cell_new_population))
    new_population = new_population(sorted_fitnesses)
    new_population = new_population(mslice[1:population_size])
    #new_population
end
