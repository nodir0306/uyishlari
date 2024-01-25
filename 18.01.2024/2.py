class ElementDublicationError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class MyList(list):
        def append(self,son):
            if son not in self:
                super().append(son)
            else:
                raise ElementDublicationError("Qandaydir xato yuz berdi")
try:
    son = MyList((2,5,8))
    son.append(2)
    print(son)
except ElementDublicationError:
    print("Qandaydir xato yuz berdi")