def getTotalPopulation(cities):
    totalpopulation=0
    for i  in range(len(cities)):
        totalpopulation=totalpopulation+cities[i][2]
    return totalpopulation
cities = [ ["Pittsburgh", "Allegheny", 302407],
           ["Philadelphia", "Philadelphia", 1584981],
           ["Allentown", "Lehigh", 123838],
           ["Erie", "Erie", 97639],
           ["Scranton", "Lackawanna", 77182] ]
print(getTotalPopulation(cities))
