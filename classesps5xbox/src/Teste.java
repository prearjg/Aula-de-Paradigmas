



public class Teste {
    public static void main(String[] args) {

        //Tem-se um Xbox2 e mas deseja-se usar um controle ps5:
        SensorXbox2 adaptee = new SensorXbox2();
        ControlePS5 target = new ControlePS5();

        //Cria-se um falso sensor de PS5 que, na verdade, traduz e repassa os comandos para o Xbox em questão:
        AdaptadorPS5ParaXbox2 adapter = new AdaptadorPS5ParaXbox2(adaptee);

        //Conecta-se o controle ao adapter:
        target.Conectar(adapter);
    }
}

//Saída:
//Um novo controloe foi conectado ao sensor do Xbox.
//But stadia wins!