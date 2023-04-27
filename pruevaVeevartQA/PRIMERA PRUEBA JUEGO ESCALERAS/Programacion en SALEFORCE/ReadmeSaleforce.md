# PROGRAMACION EN SALEFORCE
## DE QUE SE TRATA 
En esta programacion se encuentra el juego de la serpiente y escalera en lenguaje apex, este tiene la misma logica que el realizado en python en donde el jugador debe de ejecutar el programa para que inicie el juego y observar los eventos que ocurran en este hasta llegar a la casilla 25
## COMO EJECUTARLO
Solo debe de tener el playground en Saleforce, copiar el programa pegarlo en su Apex Class vacia y listo, despues solo debe de ejecutarlo al seleccionar Debug y despues a "Open Execute Anonymous Window", al desplegar la ventana emergente debera de escribir el comendo de ejecucion el cual es "GAME game = new GAME();" eso llamara al constructor, el cual a su vez contiene todo el juego.
## TEST
Se realizo dos Test, el primero es para verificar que el dado este arrojando los numeros del rango del 1 al 6 de manera correcta, asi podemos determinar que la funcion este bien programada y no lance numerosos como 0 o numeros mayores que 6, ya que podia crear una ventaja al jugador a la vez que no cumpliria con una restricción impuesta. 

El segundo test consta de verificar el movimiento del jugador ya que la casilla en la que inicia el juego es 1, se debera asegurar que el jugador se encuentre en esta posicion y avance con respecto al tablero, asi si el dado lanza 3 el jugador avanzara hasta la casilla 4, en la prueba se entrega que se lanzo el dado 1, por lo que el jugador se encuentra en la casilla uno y se movera hasta la casilla 2, por lo que el resultado esperado sera 2.