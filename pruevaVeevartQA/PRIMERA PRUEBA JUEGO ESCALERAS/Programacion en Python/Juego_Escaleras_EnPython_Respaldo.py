# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 09:21:21 2023

@author: Weav9
"""
import random
import unittest

jugador = 1
numero_turno = 0
Escalera1 = 3 #Esta escalera haciende de la 3 a la 11 osea 8 sube 8 casillas
Escalera2 = 6 #Esta escalera haciende de la 6 a la 17 osea 11 sube 11 casillas
Escalera3 = 9 #Esta escalera haciende de la 9 a la 18 osea 9 sube 9 casillas
Escalera4 = 10 #Esta escalera haciende de la 10 a la 12 osea 2 sube 2 casillas
Serpiente1 = 14 #Esta serpiente desciende desde la 14 a la 4 osea 10 casillas
Serpiente2 = 19 #Esta serpiente desciende desde la 19 a la 8 osea 11 casillas
Serpiente3 = 22 #Esta serpiente desciende desde la 22 a la 20 osea 2 casillas
Serpiente4 = 24 #Esta serpiente desciende desde la 24 a la 16 osea 8 casillas

#INTERACCIÓN CON EL USUARIO PARA INICIAR EL JUEGO
comienza_juego=int(input("presione el 1 para lanzar el dado y comenzar el juego: "))

def dado():
    return random.randint(1, 6)

if comienza_juego==1:
    while jugador < 25:
        numero_turno += 1
        lanzamientoDado = dado()
        jugador = jugador+lanzamientoDado
        print(f"Turno {numero_turno}: lanzaste el dado y sacaste un {lanzamientoDado}.")
#-------ACCION CUANDO EL JUGADOR SE ENCUENTRA CON UNA ESCALERA-------------------------------------------------------------------------------
        if jugador == Escalera1:
            jugador = jugador+8
            print("¡Felicidades! Subiste por una escalera haciendes hasta la casilla 11")
        if jugador == Escalera2:
            jugador = jugador+11
            print("¡Felicidades! Subiste por una escalera haciendes hasta la casilla 17")
        if jugador == Escalera3:
            jugador = jugador+9
            print("¡Felicidades! Subiste por una escalera haciendes hasta la casilla 18")
        if jugador == Escalera4:
            jugador = jugador+2
            print("¡Felicidades! Subiste por una escalera haciendes hasta la casilla 12")
#-------ACCION CUANDO EL JUGADOR SE ENCUENTRA CON UNA SERPIENTE-------------------------------------------------------------------------------
        if jugador == Serpiente1:
            jugador = jugador-10
            print("¡OH NO! Te encontraste con una serpiente bajas hasta la casilla 4")
        if jugador == Serpiente2:
            jugador = jugador-11
            print("¡OH NO! Te encontraste con una serpiente bajas hasta la casilla 8")
        if jugador == Serpiente3:
            jugador = jugador-2
            print("¡OH NO! Te encontraste con una serpiente bajas hasta la casilla 20")
        if jugador == Serpiente4:
            jugador = jugador-8
            print("¡OH NO! Te encontraste con una serpiente bajas hasta la casilla 16")
        if jugador > 25:
            print("¡PASASTE LA CASILLA 25!")
        if jugador <= 25:
            print(f"Avanzaste al cuadro {jugador}.\n")
    # Mostrar resultado final
    print(f"Felicidades, ¡GANASTE EN {numero_turno} TURNOS!")
    
"""
TEST PARA LOS MODULOS DE DADO Y COMIENZA JUEGO 

class TestDado(unittest.TestCase):
    
    def test_dado(self):
        for _ in range(1000):
            valor = dado()
            self.assertTrue(valor >= 1 and valor <= 6)

if __name__ == '__main__':
    unittest.main()


class TestComienzaJuego(unittest.TestCase):
    
    def test_comienza_juego(self):
        # Forzamos el valor de "dado" a 6 para que el jugador llegue a la casilla 25 en un solo turno
        comienza_juego(dado=lambda: 6)
        self.assertEqual(jugador, 25)

if __name__ == '__main__':
    unittest.main()
"""