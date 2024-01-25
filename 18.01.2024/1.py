class MyList(list):
    def remove(self,son):
      for i in range(self.count(son)):
              super().remove(son)
son = MyList((2,2,2,2,2,2,2,2,2,2))
son.remove(2)
print(son)