class MyList(list):
    def save(self, son):
        for i in  self:
            if son != i:
                i =  " "

lst = MyList((1, 2, 2, 3, 4, 5, 1, 1, 1, 8))
lst.save(1)
print(lst)
