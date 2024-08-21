alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

index = 1;

for alien in aliens:
    print(f"\nAlien{index} : ");
    index+=1;
    for key, value in alien.items():
        print(f"Key: {key}")
        print(f"Value: {value}")
        
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}


favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell'],
}

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

