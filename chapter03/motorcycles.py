motorcycles = ['honda', 'yamaha', 'suzuki']
#motorcycles[0] = 'ducati'
print(motorcycles)

""" motorcycles.append('ducati')
print(motorcycles) """

motorcycles.insert(2, 'ducati')
print(motorcycles)

""" del motorcycles[2]
print(motorcycles) """


""" popped_motor = motorcycles.pop()
print(motorcycles)
print(popped_motor)

pop_first_elem = motorcycles.pop(0)
print(motorcycles)
print(pop_first_elem) """

#remove by value
""" motorcycles.remove('yamaha')
print(motorcycles) """

cars = ['bmw', 'audi', 'toyota', 'subaru']
""" cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)
 """

sorted_cars = sorted(cars)
print(sorted_cars)
print(cars)

cars.sort()
cars.reverse()

print(len(cars))