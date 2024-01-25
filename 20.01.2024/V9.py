class Employee:
    def __init__(self,surname:str,position:str,salary:int):
        self.surname = surname
        self.position = position
        self.salary = salary
class Enterprice_Employe(Employee):
    def __init__(self, surname: str, position: str, salary: int,rating:int):
        super().__init__(surname, position, salary)
        self.rating = rating
        if self.rating >=65 and self.rating < 75:
            self.salary += self.salary / 100 * 20
        elif self.rating >=75 and self.rating <95:
            self.salary += self.salary / 100 * 40
        elif self.rating >=95 and self.rating <=100:
            self.salary += self.salary / 100 * 60
    def info(self):
        return f"""
Familiya: {self.surname}
Lavozimi: {self.position}
Oyligi:   {self.salary}
    """
    
res1 = Enterprice_Employe("Savbatov","Ishchi",120,65)
res2 = Enterprice_Employe("Egamberdiyev","Ishchi",1200,75)
res3 = Enterprice_Employe("Bekmuradov","Ishchi",140,95)
res4 = Enterprice_Employe("Rajabov","Ishchi",170,90)
res5 = Enterprice_Employe("Axmatova","Ishchi",220,100)
print(res1.info())
print(res2.info())
print(res3.info())
print(res4.info())
print(res5.info())