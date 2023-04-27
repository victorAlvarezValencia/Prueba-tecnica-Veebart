## SOPA DE LETRAS
# QUE ES
En este programa se realizo una sopa de letras, la cual basicamente busca encontrar las palabras que se requieran dentro de 1 arreglo descrito, asi al buscar las palabras que se requieran el programa debe de indicar en donde se ubican estas palabras dentro del arreglo ademas en caso contrario debe de mostrar si no se pudo encontrar las palabras deseadas. 

Ademas como extra se añada de que puede leer dos palabras ubicadas en diferentes filas asi si hay ['S O L', 'S O L','N U T'] dara la ubicación de los dos Sol aunque se hubiquen en diferente filas.

# COMO FUNCIONA
Esta función recibe como parámetros la sopa de letras en formato de lista de strings, por lo que no se puede ingresar en la consola, esto para evitar que el usuario ingrese parametros incorrectos que generen un error, para esto se hace una interacción con el usuario para que solamente seleccione una de las 4 opciones, cada opcion tiene una sopa de letras diferentes, para observar los distintos casos que se plantearon. Ademas cuenta con una lista de palabras a buscar en la sopa de letras. La función devuelve la ubicación de cada letra de cada palabra encontrada en la sopa de letras.

Primero, la función convierte la sopa de letras en una matriz de caracteres, eliminando los espacios en blanco. Luego, se inicializa un diccionario que contendrá las posiciones de las letras de cada palabra encontrada en la sopa de letras. A continuación, se buscan las palabras en las filas y en las columnas de la matriz, utilizando el método index para buscar la primera letra de la palabra en cada fila o columna. Si se encuentra la palabra, se agregan las posiciones de cada letra al diccionario correspondiente.

Finalmente, se imprime la ubicación de cada letra de cada palabra encontrada en la sopa de letras, o se indica que la palabra no se encontró si corresponde.
# COMO EJECUTARLA
Para ejecutarla solo debe de abrir su copilador de preferencia, copiar el codigo python y despues ejecutarlo, cuando esto ocurra se abrira la terminal o consola, pidiendo que seleccione entre 1, 2, 3 y 4, esto son las distintas sopas de letras posible. Solo debe de seleccionar el que desee y posteriormente de manera automatica mostrara la ubicacion de las palabras que aparecen en la opcion seleccionada.