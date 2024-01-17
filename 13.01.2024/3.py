class countries:
    def __init__(self, name, capital, population, land_area, prezident):
        self.name = name
        self.capital = capital
        self.population = population
        self.land_area = land_area
        self.prezident = prezident

    def info(self):
        return f"Nomi: {self.name}, Poytaxti: {self.capital}, Aholi soni: {self.population}, Yer maydoni: {self.land_area}, Prezidenti: {self.prezident}"

malumotlar = []

for i in range(1, 11):
    name = input("Davlat nomi: ")
    capital = input("Poytaxti: ")
    population = input("Aholi soni: ")
    land_area = int(input("Yer maydoni: "))
    prezident = input("Prezidenti: ")

    malumot = countries(name, capital, population, land_area, prezident)
    malumotlar.append(malumot)


sorted_countries = sorted(malumotlar, key=lambda x: x.name)


for malumot in sorted_countries:
    print(malumot.info())
