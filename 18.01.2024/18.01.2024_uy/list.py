class ListEmptyError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class MyList(list):
    def find(self):
        if len(self) == 0:
            raise ListEmptyError("Qandaydir xato yuz berdi")
        
        max_count = 0
        most_element = None

        for i in self:
            count_i = self.count(i)
            if count_i > max_count:
                max_count = count_i
                most_element = i

        return most_element
try:
    lst = MyList([])
    result = lst.find()
    print("Eng ko'p takrorlangan element:", result)
except ListEmptyError:
    print("Qandaydir xato yuz berdi")
