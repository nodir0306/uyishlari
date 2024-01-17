class Transport:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def GetInfo(self):
        return f"""
Brendi: {self.brand}
Modeli: {self.model}
Rangi: {self.color}
    """

    def SetBrand(self, brand):
        self.brand = brand

    def SetModel(self, model):
        self.model = model

    def SetColor(self, color):
        self.color = color


class Car(Transport):
    def __init__(self, brand, model, color, speed, seat_count, manufacture_date):
        super().__init__(brand, model, color)
        self.speed = speed
        self.seat_count = seat_count
        self.manufacture_date = manufacture_date

    def GetInfo(self):
        info = super().GetInfo()
        return f"""
{info}
Tezligi: {self.speed}
Sotildi: {self.seat_count}
Yili: {self.manufacture_date}
    """

    def SetSpeed(self, speed):
        self.speed = speed

    def SetSeatCount(self, seat_count):
        self.seat_count = seat_count

    def SetManufactureDate(self, manufacture_date):
        self.manufacture_date = manufacture_date


class Truck(Transport):
    def __init__(self, brand, model, color, capacity):
        super().__init__(brand, model, color)
        self.capacity = capacity

    def GetInfo(self):
        info_k = super().GetInfo()
        return f"""
{info_k}
Capasity: {self.capacity}
    """

    def SetCapacity(self, capacity):
        self.capacity = capacity


transport_instance = Transport("BMW", "M5", "Black")
truck_instance = Truck("Volvo", "VNL", "Blue", 1500)
car_instance = Car("Toyota", "Camry", "Silver", 150, 5, "2024")

print(transport_instance.GetInfo())
print(truck_instance.GetInfo())
print(car_instance.GetInfo())
