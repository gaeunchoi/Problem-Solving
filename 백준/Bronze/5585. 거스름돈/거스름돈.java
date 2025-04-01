import java.util.Scanner;
 
public class Main {
    public static int price;
    public static int count;
    
    public static int[] coinArr = {500, 100, 50, 10, 5, 1};
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        price = 1000 - sc.nextInt();
 
        for(int coin:coinArr) {
            getCount(coin);
        }
        
        System.out.println(count);
    }
    
    public static void getCount(int coin) {
        count += (price / coin);
        price = price - (coin * (price / coin));
    }
}
