class Texnika:
    def __init__(self,brand,model,type):
        self.brand = brand
        self.model = model
        self.type = type
        
    def info(self):
        return f"""
Brand: {self.brand}
Model: {self.model}
Type:  {self.type}
    """

class Notebooks(Texnika):
    def __init__(self, brand, model, type,vidicard,ram,display):
        super().__init__(brand, model, type)
        self.vidicard = vidicard
        self.ram = ram
        self.display = display
    def more_info(self):
        return f"""
Brand:          {self.brand}
Model:          {self.model}
Type:           {self.type}
Vidio Card:     {self.vidicard}
Ram:            {self.ram}
Display:        {self.display}
    """

class Television(Texnika):
    def __init__(self, brand, model, type,size,display):
        super().__init__(brand, model, type)
        self.size = size
        self.display = display
        def more_info(self):
            return f"""
Brand:          {self.brand}
Model:          {self.model}
Type:           {self.type}
Size            {self.size}
Display:        {self.display}
    """
    
class Smartphones(Texnika):
    def __init__(self, brand, model, type,size,sim_count):
        super().__init__(brand, model, type)
        self.size = size
        self.sim_count = sim_count
    def more_info(self):
        return f"""
Brand:          {self.brand}
Model:          {self.model}
Type:           {self.type}
Size            {self.size}
Sim Count:      {self.sim_count}
    """


p = Notebooks("Samsum","J5 Prime","Maishiy",47,2)
print(p.more_info())