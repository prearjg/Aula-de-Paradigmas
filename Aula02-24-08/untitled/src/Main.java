import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        int qtd1 = 0, qtd2 = 0, qtd3 = 0, qtd5 = 0, qtd9 = 0;
        int code = 0;
        int qtd = 0;
        System.out.println("A tabala de preço é:\n1 - 0,50"
        +"\n2 - 1,00\n3 - 4,00\n5 - 7,00\n9 - 8,00\n0 - SAIR");
        double valor = 0;
        do {
            System.out.println("Digite o código");
            code = teclado.nextInt();
            if(code == 0){
                break;
            }
            System.out.println("Digite a quantidade");
            qtd = teclado.nextInt();
            switch (code){
                case 0:
                    break;
                case 1:
                    valor += 0.50 * qtd;
                    qtd1++;
                    break;
                case 2:
                    valor += 1 * qtd;
                    qtd2++;
                    break;
                case 3:
                    valor += 4 * qtd;
                    qtd3++;
                    break;
                case 5:
                    valor += 7 * qtd;
                    qtd5++;
                    break;
                case 9:
                    valor += 9 * qtd;
                    qtd9++;
                    break;
                default:
                    System.out.println("Valor incorreto");
            }


        }while(code!=0);

        System.out.println("As quantidades foram:\nCodigo 1: "+ qtd1 +
                "\nCodigo 2: "+ qtd2 +"\nCodigo 3: " + qtd3 +"\nCodigo 5: "+ qtd5
                +"\nCodigo 9: "+ qtd9 +"\nO valor total foi de: "+ valor);


        }
    }