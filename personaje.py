import random
import sys

class Personaje:
    def __init__(self, nombre:str, nivel:int, experiencia:int):
        self.nombre = nombre
        self.nivel = nivel
        self.experiencia = experiencia
        self.prob = 0

# b. Getter de estado.
    @property
    def estado(self):
        return f'Nombre: {self.nombre}, Nivel: {self.nivel}, Experiencia: {self.experiencia}'
# c. Setter de estado.
    @estado.setter
    def estado(self,estado:int):
        self.experiencia += estado

    def experiencia_nivel(self, experiencia):
        calc_exp = self.experiencia + experiencia
        calc_nivel = calc_exp // 100 + self.nivel
        self.experiencia = calc_exp % 100
        if  calc_exp < 1 and calc_nivel < 1:
            self.nivel = 1
            self.experiencia = 0
        elif  calc_exp < 1 and calc_nivel >= 1:
            self.experiencia = 0
            self.nivel = calc_nivel
        else:
            self.nivel = calc_nivel
            self.experiencia

# d. Sobrecarga para comparar “menor que” .
    def __lt__(self,orco):
        return  self.nivel < orco.nivel

# e. Sobrecarga para comparar “mayor que”.
    def __gt__(self,orco):
        return  self.nivel > orco.nivel

# f. Sobrecarga para comparar “igual que” (opcional).
    def __eq__(self,orco):
        return  self.nivel == orco.nivel
    
# h. Método que muestra diálogo de enfrentamiento al orco (incluyendo probabilidad de ganar) y retorna opción escogida por el jugador (opcional).
nombre = input('¡Bienvenido a Gran Fantasía!\nPor favor indique nombre de su personaje: ')
personaje_1 = Personaje(nombre,1,0)
orco =  Personaje("Orco", 1, 0)

# Asignación de experiencia mediante el estado
personaje_1.estado=50

# g. Método de instancia que retorna la probabilidad de la instancia actual de ganar respecto de otra instancia (opcional).
def probabilidad_personaje(personaje_1,orco):
    if personaje_1 < orco:
        orco.prob = 0.66
        personaje_1.prob = 0.33
    elif personaje_1 > orco:
        orco.prob = 0.33
        personaje_1.prob = 0.66
    else:
        orco.prob = 0.5
        personaje_1.prob = 0.5

probabilidad_personaje(personaje_1,orco)

print(f'''  NOMBRE: {(personaje_1.nombre).upper()}, NIVEL: {personaje_1.nivel}, EXP: {personaje_1.experiencia}
            ¡Oh no!, ¡Ha aparecido un Orco!
            Con tu nivel actual, tienes {personaje_1.prob*100}% de probabilidades de ganarle al Orco.
            Si ganas, ganarás 50 puntos de experiencia y el orco perderá 30.
            Si pierdes, perderás 30 puntos de experiencia y el orco ganará 50.''')

def combate(personaje_1,orco):
    while True:
        accion = int(input('\n¿Qué deseas hacer?\n1. Atacar\n2. Huir\n3. Salir\n'))
        if accion == 1:
            prob_comb = random.uniform(0,1)
            if prob_comb <= personaje_1.prob:
                personaje_1.experiencia_nivel(50)
                orco.experiencia_nivel(-30)
                print(f'''  ¡Le has ganado al orco, felicidades!
                            ¡Recibirás 50 puntos de experiencia!
                            NOMBRE: {(personaje_1.nombre).upper()} NIVEL: {personaje_1.nivel} EXP: {personaje_1.experiencia} 
                            NOMBRE: Orco NIVEL: {orco.nivel} EXP: {orco.experiencia} ''')
            else:
                personaje_1.experiencia_nivel(-30)
                orco.experiencia_nivel(50)
                print(f'''  ¡Oh no! ¡El orco te ha ganado!
                            ¡Has perdido 30 puntos de experiencia!
                            NOMBRE: {(personaje_1.nombre).upper()} NIVEL: {personaje_1.nivel} EXP: {personaje_1.experiencia} 
                            NOMBRE: Orco NIVEL: {orco.nivel} EXP: {orco.experiencia} ''')
        elif accion == 2:                    
            print(f'¡Escapastes del combate contra el Orco!\nNOMBRE: {(personaje_1.nombre).upper()} NIVEL: {personaje_1.nivel} EXP: {personaje_1.experiencia}')
        else:
            exit()
combate(personaje_1,orco)
