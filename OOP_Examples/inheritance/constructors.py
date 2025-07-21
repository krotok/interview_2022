class Geom:
    def __init__(self,x1,x2,y1,y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        print(f"print from {self.__class__}")

class Line(Geom):
    def drow(self):
        print("Drow Line")

class Rect(Geom):
    def __init__(self, x1, x2, y1, y2, fill = None):
        # Так мы явно вызываем init отцовского класса и передаём ему наш объеккт и все поля. Однако это делать не рекомендуется ,
        # так как имя отцовского класса может измениться
        #Geom.__init__(self, x1, x2, y1, y2)

        #Лучше использовать super(), с который не нужно передавать сам объект т.к. super() Возвращает ссылку на
        # объект-посредник через который происходит вызов объектов базового класса.
        super().__init__( x1, x2, y1, y2)
        self.fill = fill
        print(f"Class:{self.__class__}")

l = Line(0,0,10,20)
r = Rect(0,0,20,30)
print(l.__dict__)
print(r.__dict__)







