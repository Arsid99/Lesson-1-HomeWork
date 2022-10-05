from random import randint


class House:
    def __init__(self, number_house):
        self.population = randint(1, 100)
        self.number_house = number_house


class Street:
    def __init__(self, number_street, number_house):
        self.houses = []
        self.number_street = number_street
        self.number_house = number_house
        for house in range(self.number_house):
            self.houses.append(House(len(self.houses) + 1))


class City:
    def __init__(self, city_name='Kharkov', min_house_par=5, max_house_par=20, min_street_par=1, max_street_par=8):
        self.count_house = randint(min_house_par, max_house_par)
        self.city_name = city_name
        self.streets = []
        self.number_of_street = randint(min_street_par, max_street_par)

    @property
    def population(self):
        population = 0
        for street in self.streets:
            for house in street.houses:
                population += house.population
        return population

    def fill_the_city(self):
        for street in range(self.number_of_street):
            self.streets.append(Street(len(self.streets) + 1, randint(5, 20)))

    def add_street(self):
        while len(self.streets) < self.number_of_street:
            self.streets.append(Street(len(self.streets) + 1, self.count_house))

    def delete_street(self, street_num):
        self.streets.pop(street_num - 1)

    def print_the_city(self):
        print('Street', 'House', 'Population')
        for street in self.streets:
            for house in street.houses:
                print(street.number_street, house.number_house, house.population, sep='   ->   ')


city = City()
city.fill_the_city()
city.print_the_city()
print(f'The population of {city.city_name} is approximately {city.population} people')
