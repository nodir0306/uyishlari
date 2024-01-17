class Soldat:
    def __init__(self,ism,familiya,yosh,jinsi,boy,vazn):
        self.ism = ism
        self.familiya = familiya
        self.yosh = yosh
        self.jinsi = jinsi
        self.boy = boy
        self.vazn = vazn
    def GetInfo(self):
        if self.yosh > 18 and self.jinsi == 0:
            return f"Ismi: {self.ism}, Familiyasi: {self.familiya}, Jinsi: {self.jinsi}, Yoshi: {self.yosh}"
    def Yonalish(self):
        if self.boy  < 150 and self.vazn < 75:
            return "Piyoda askarlariga"
        else: 
            return "Tank qo'shinlariga"
class Armiya(Soldat):
    def __init__(self, ism, familiya, yosh, jinsi, boy, vazn,xizmat_mudiri):
        super().__init__(ism, familiya, yosh, jinsi, boy, vazn)
        self.xizmat_mudiri = xizmat_mudiri
    def GetInfo(self):
        soldat_info = super().GetInfo()
        return f"{soldat_info} Xizmat mudiri {self.xizmat_mudiri}"
soldat1 = Soldat("Nodir","Savbatov",20,0,180,70)

print(soldat1.GetInfo())
print(soldat1.Yonalish())