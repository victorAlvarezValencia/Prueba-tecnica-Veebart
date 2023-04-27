# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 14:00:57 2023

@author: Weav9
"""


numeroSopa=int(input("Seleccione entre 1,2,3 y 4 para seleccionar una sopa de letras:  "))


if numeroSopa == 1:
    sopa_de_letras = ["S O L", "U N O", "N U T"]
    palabras_a_buscar = ["SUN", "SOL", "LOT", "ONU", "RAY"]
if numeroSopa == 2:
    sopa_de_letras = ["P B L", "I L I", "N O T"]
    palabras_a_buscar = ["PIN", "BLO", "LIT", "NOT", "ILI"]
if numeroSopa == 3:
    sopa_de_letras = ["G O L", "A L O", "S U T"]
    palabras_a_buscar = ["GAS", "GOL", "OLU", "LOT", "ALO"]
if numeroSopa == 4:
    sopa_de_letras = ["N I Y", "N I Y", "P T S"]
    palabras_a_buscar = ["NIY", "SOL", "LOT", "ONU", "YES"]

def buscar_palabras(sopa_de_letras, palabras_a_buscar):
    matriz = [fila.split() for fila in sopa_de_letras]
    palabras_encontradas = []
    palabras_noEncontradas = []
    
    # Inicializar un diccionario para guardar las ubicaciones de cada letra
    ubicaciones_letras = {}
    for i, fila in enumerate(matriz):
        for j, letra in enumerate(fila):
            if letra not in ubicaciones_letras:
                ubicaciones_letras[letra] = []
            ubicaciones_letras[letra].append((i, j))
    
    # Buscar las palabras en la matriz
    resultados = {}
    for palabra in palabras_a_buscar:
        letras_palabra = list(palabra)
        if letras_palabra[0] not in ubicaciones_letras:
            # La primera letra no está en la matriz
            resultados[palabra] = []
            continue
        
        # Buscar la palabra en filas y columnas
        ubicaciones_palabra = []
        for i, j in ubicaciones_letras[letras_palabra[0]]:
            # Buscar horizontalmente
            if j + len(letras_palabra) <= len(matriz[i]) and \
               letras_palabra == matriz[i][j:j+len(letras_palabra)]:
                ubicaciones_palabra.append([(i, j+x) for x in range(len(letras_palabra))])
            
            # Buscar verticalmente
            elif i + len(letras_palabra) <= len(matriz) and \
                 letras_palabra == [matriz[i+x][j] for x in range(len(letras_palabra))]:
                ubicaciones_palabra.append([(i+x, j) for x in range(len(letras_palabra))])
        
        # Guardar las ubicaciones de la palabra
        if ubicaciones_palabra:
            resultados[palabra] = ubicaciones_palabra
        else:
            resultados[palabra] = []
    
    for palabra in palabras_a_buscar:
        # Buscamos en la filas 
        for fila in matriz:
            fila_str = "".join(fila)
            if palabra in fila_str:
                # Obtener la posición inicial y final de la palabra en la fila
                inicio = fila_str.index(palabra)
                fin = inicio + len(palabra) - 1
                # Guardar las posiciones de cada letra de la palabra
                posiciones = [(fila.index(fila[i]), i) for i in range(inicio, fin+1)]
                # Añadir la palabra encontrada a la lista de palabras encontradas
                palabras_encontradas.append((palabra, posiciones))
                break
            
        # Si la palabra ya fue encontrada, saltar a la siguiente
        if palabra in [p[0] for p in palabras_encontradas]:
            continue
        
        # Buscar en las columnas
        for i in range(len(matriz[0])):
            columna_str = "".join([fila[i] for fila in matriz])
            if palabra in columna_str:
                # Obtener la posición inicial y final de la palabra en la columna
                inicio = columna_str.index(palabra)
                fin = inicio + len(palabra) - 1
                # Guardar las posiciones de cada letra de la palabra
                posiciones = [(j, i) for j in range(inicio, fin+1)]
                # Añadir la palabra encontrada a la lista de palabras encontradas
                palabras_encontradas.append((palabra, posiciones))
                break
            
        # Si las palabras no fueron encontradas se almacenaran en este arreglo 
        if not palabra in [p[0] for p in palabras_encontradas]:
            palabras_noEncontradas.append(palabra)
            
    for palabra, ubicaciones in resultados.items():
        if not ubicaciones:
            print(f"No se encontró la palabra '{palabra}'")
        else:
            print(f"La palabra '{palabra}' se encontró en las siguientes ubicaciones:")
            for ubicacion in ubicaciones:
                print(ubicacion)
        


buscar_palabras(sopa_de_letras, palabras_a_buscar)
