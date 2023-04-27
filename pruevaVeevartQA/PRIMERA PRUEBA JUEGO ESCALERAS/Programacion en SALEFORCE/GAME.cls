public class GAME {
    
    public game() {
        comenzar_juego();
    }
   
    
    public integer actualizar_Jugador(integer dado, integer jugador){
        Jugador = jugador + dado;
        return jugador;
    }
    
    public integer lanzardado(){
        integer min = 1;
        integer max = 6;
		integer int_random = (integer)Math.floor(Math.random()*(max - min + 1) + min);        
        return int_random;
    }
    
    
    public void comenzar_juego(){
        integer jugador = 1;
        integer dado = 0;
        boolean Victoria = true;
        integer numero_turno = 0;
        while (jugador < 25){
            dado = lanzardado();
            numero_turno += 1;
            jugador = actualizar_Jugador(dado, jugador);
            System.debug('Turno ' + numero_turno + ': lanzaste el dado y sacaste un ' + dado + '.');
        	if (jugador == 3) {
                jugador += 8;
                System.debug('¡Felicidades! Subiste por una escalera hasta la casilla 11.');
        	}
        	if (jugador == 6) {
            	jugador += 11;
            	System.debug('¡Felicidades! Subiste por una escalera hasta la casilla 17.');
        	}
        	if (jugador == 9) {
            	jugador += 9;
            	System.debug('¡Felicidades! Subiste por una escalera hasta la casilla 18.');
        	}
        	if (jugador == 10) {
            	jugador += 2;
            	System.debug('¡Felicidades! Subiste por una escalera hasta la casilla 12.');
        	}
        	if (jugador == 14) {
            	jugador -= 10;
            	System.debug('¡OH NO! Te encontraste con una serpiente y bajaste hasta la casilla 4.');
        	}
        	if (jugador == 19) {
            	jugador -= 11;
            	System.debug('¡OH NO! Te encontraste con una serpiente y bajaste hasta la casilla 8.');
        	}
        	if (jugador == 22) {
            	jugador -= 2;
            	System.debug('¡OH NO! Te encontraste con una serpiente y bajaste hasta la casilla 20.');
        	}
        	if (jugador == 24) {
            	jugador -= 8;
            	System.debug('¡OH NO! Te encontraste con una serpiente y bajaste hasta la casilla 16.');
        	}
            if (jugador > 25){
                System.debug('¡PASASTE LA CASILLA 25!');
            }
            if (jugador <= 25){
                System.debug('Has Avanzado al cuadro ' + jugador);
            }
        }
        System.debug('Felicidades, ¡GANASTE EN ' + numero_turno + ' TURNOS!');
    }
}
