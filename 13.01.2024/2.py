"""
Mashina nomli class yarating. Ushbu classning elementlari nomi, turi (yengil, yuk avtomobili), narxi, ishlab_chiqarilgan_yili.
Mashinaning malumot nomli methodi bor unda mashina xaqida malumot chiqib keladi. 10 ta mashina xaqida malumot berilgan
mashinalarni ishlab chiqarilgan yili 
bo'yicha saralab ekranga chop eting. Mashinani narxi kiritilmaganda default 4.000$ qiymatni berib keting.
"""
class Car:
    def __init__ (self,name,type,year,cost = 4000):
        self.name = name
        self.type = type
        self.year = year
        self.cost = cost
    def info(self):
        return f"Car name: {self.name},  Car type: {self.type},  Car year: {self.year}, Car cost: {self.cost}"

cars = []
for i in range(1,11):
    name = input("Car name: ")
    type = input("Car type: ")
    year = int(input("Year: "))
    cost = float(input("Cost: "))
    
    car = Car(name,type,year,cost)
    cars.append(car)
    
sorted_cars = sorted(cars,key=lambda x:x.year)

for car in sorted_cars:
    print(car.info())    
