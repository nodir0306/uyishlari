class Transport:
    def __init__(self,brand,model,type):
        self.brand = brand
        self.model = model
        self.type = type
    def info(self):
        return f"""
Brand:   {self.brand}
Model:   {self.model}
Type:    {self.type}
    """
        
class ElectroCars(Transport):
    def __init__(self, brand, model, type,battery_life,chargin_time):
        super().__init__(brand, model, type)
        self.battery_life = battery_life
        self.chargin_time = chargin_time
    def more_info(self):
        return f"""
Brand:         {self.brand}
Model:         {self.model}
Type:          {self.type}
Battery life:  {self.battery_life}
Chargin time:  {self.chargin_time}
    """
    
class SportCars(Transport):
    def __init__(self, brand, model, type,motor,color):
        super().__init__(brand, model, type)
        self.motor = motor
        self.color = color
    def more_info(self):
        return f"""
Brand:         {self.brand}
Model:         {self.model}
Type:          {self.type}
Motor:         {self.motor}
Color:         {self.color}
    """
    
class Truck(Transport):
    def __init__(self, brand, model, type,motor,height,long,weight):
        super().__init__(brand, model, type)
        self.motor = motor
        self.height = height
        self.long = long
        self.weight = weight
    def more_info(self):
        return f"""
Brand:         {self.brand}
Model:         {self.model}
Type:          {self.type}
Motor:         {self.motor}
Height:        {self.height}
Weight:`       {self.weight}
Long:          {self.long}
    """