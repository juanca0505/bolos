import random

#Definimos la clase Game. Esta clase representa un juego de bolos completo.
# El constructor de la clase Game crea una lista vacía para almacenar los frames del juego y establece el siguiente frame en 0.

class Game:
    def __init__(self):
        self.frames = []
        self.next_frame = 0

#esta funcion permite lanzar bolos en el juego
#Recibe como parámetro el número de bolos derribados y los agrega al frame actual. También actualiza el siguiente frame.
    def roll(self, pins):
        self.frames[self.next_frame].add_roll(pins)
        self.next_frame = (self.next_frame + 1) % 10
#esta funcion calcula la puntuación del juego. Recorre la lista de frames y agrega la puntuación de cada frame a la puntuación total.

    def score(self):
        score = 0
        for frame in self.frames:
            score += frame.score()
        return score

# Esta clase frame representa un frame de bolos individual, el constructor de esta clase cree una lista para almacenar del frame
# y establece el número de bolos derribados en el parámetro pins
class Frame:
    def __init__(self, pins):
        self.rolls = []
        self.pins = pins
#esta funcion agrega un roll al frame
    def add_roll(self, pins):
        self.rolls.append(pins)

    def score(self):
        if len(self.rolls) == 2:
            if self.rolls[0] + self.rolls[1] == 10:
                return 10 + self.rolls[2] if len(self.rolls) > 2 else 10
            else:
                return self.rolls[0] + self.rolls[1]
        else:
            return sum(self.rolls)
#Esta clase hereda de la clase Frame y representa un frame normal de bolos, con dos rolls
class NormalFrame(Frame):
    def __init__(self, pins):
        super().__init__(pins)
#Esta clase hereda de la clase Frame y representa el décimo frame de bolos, que puede tener tres rolls
class TenthFrame(Frame):
    def __init__(self, pins):
        super().__init__(pins)


