from human import Human
class Student(Human):
    def __init__(self, canvas, x, y, name, gen, g, v):
        super().__init__(canvas, x, y, name, gen) 
        self.var = v
        
    def __drawName(self):
        name = f"{self._name.split()[0]} {self._name.split()[1][0]}. {self._name.split()[2][0]}."
        self.canvas.create_text(20, 390, text=
        f'{self._name}, {self.__group}, №{self.__var}',
        font="Times 18", anchor=W, fill="green")