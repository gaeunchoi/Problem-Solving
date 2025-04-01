import java.util.*;
import java.math.*;

class Result {
    public BigDecimal pow(BigDecimal a, int b){
        if( b == 0 ) return a.ONE;
        else if( b == 1 ) return a;
        else if( b % 2 == 1 ){      // 지수가 홀수면 a*a^b-1으로 b를 짝수로 ㄱ
            return a.multiply(pow(a,b-1));
        }
        else {         // 지수가 짝수니까 분할
            BigDecimal k = pow(a, b/2);
            return k.multiply(k);
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        Result res = new Result();

        double a = scanner.nextDouble();
        int b = scanner.nextInt();


        // BigDecimal의 매개변수는 문자열로 와용
        BigDecimal bd = new BigDecimal(String.valueOf(a));

        BigDecimal result = res.pow(bd, b);

        System.out.println(result.toPlainString());
    }
}