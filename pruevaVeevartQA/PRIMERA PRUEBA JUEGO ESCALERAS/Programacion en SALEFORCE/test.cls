@isTest
public class GameTest {
    @isTest
    static void testGame(){
        GAME game = new game();
        Integer dado = game.lanzardado();
        Assert.isTrue(dado>=1 && dado<=6);
    }
    @isTest
    static void testGame1(){
        GAME game = new game();
        Integer jugador = game.actualizar_Jugador(1, 1);
        Assert.areEqual(2,jugador);
    }
 
}