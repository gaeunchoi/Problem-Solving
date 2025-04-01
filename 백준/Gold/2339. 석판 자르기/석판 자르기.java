import java.util.*;

class Point {
    int x;
    int y;

    public Point(int x, int y){
        this.x = x;
        this.y = y;
    }

    public int getX(){
        return this.x;
    }

    public int getY(){
        return this.y;
    }
}

public class Main {
    // main에서 입력받은 배열, x의 시작점, y의시작점, x의 끝점, y의 끝점, 방향(가로 0, 세로 1)순서대로 인자값 받음
    public static int cut(int stone[][], int sx, int sy, int ex, int ey, int direction){

        // 가변 길이 배열 생성. Point 객체를 타입으로 지정해줌(x,y값을 받아 저장함)
        Vector<Point> pv = new Vector<Point>();
        int gem = 0;    // 보석 개수 카운트할 변수 gem

        // 입력받은 배열 전부 돌아보자
        for(int i = sx ; i < ex ; i++ ){
            for(int j = sy ; j < ey ; j++ ){
                // 만약 불순물이 걸리면
                if(stone[i][j] == 1) {
                    // 불순물의 좌표를 가변 길이 배열인 pv에 넣어줌
                    pv.add(new Point(i,j));
                }
                // 만약 보석이 걸리면
                else if(stone[i][j] == 2) gem++;    // 보석의 개수 증가시켜줌
            }
        }

        if(gem == 0) return 0;  // 보석이 0개면 0 리턴함
        if(gem == 1)
            if(pv.size() == 0)
                return 1;  // 보석이 1개이고 불순물이 없다면 1 리턴함.
        if(pv.size() == 0) return 0;    // 불순물이 없다면 뭘 리턴해야할까요 ? ㅋㅋㅋㅋㅋ
        // 보석이 있는데 불순물만 없다면 ? 망한거 아닌가 ;

        //
        int result = 0;

        // 석판을 가로로 잘랐다면
        if(direction == 0){
            // for-each문으로 pv 순회
            for(Point p : pv){
                // 불순물의 x, y 좌표 받아오기
                int x = p.getX();
                int y = p.getY();

                // 불순물이 있는 라인을 자를건데 그때 보석이 있는지 확인해줄 변수
                int check = 0;

                for(int j = sy ; j < ey ; j++){
                    if(stone[x][j] == 2) check = 1;
                }

                if(check != 1) result += cut(stone, sx, sy, x, ey, 1) * cut(stone, x+1, sy, ex, ey, 1);
            }
        }

        // 석판을 세로로 잘랐다면
        else {
            // for-each문으로 pv 순회
            for(Point p : pv){
                // 불순물의 x, y 좌표 받아오기
                int x = p.getX();
                int y = p.getY();

                // 불순물이 있는 라인을 자를건데 그때 보석이 있는지 확인해줄 변수
                int check = 0;

                for(int j = sx ; j < ex ; j++){
                    if(stone[j][y] == 2) check = 1;
                }

                if(check != 1) result += cut(stone, sx, sy, ex, y, 0) * cut(stone, sx, y+1, ex, ey, 0);
            }
        }

        return result;
    }

    public static void main(String args[]){
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();

        // 배열에 석판 정보를 입력받는다
        int stone[][] = new int[20][20];
        for(int i = 0 ; i < n ; i++ ){
            for(int j = 0 ; j < n ; j++ ){
                stone[i][j] = scanner.nextInt();
            }
        }

        int result = cut(stone, 0, 0, n, n, 0) + cut(stone, 0, 0, n, n, 1);
        if(result == 0) System.out.print("-1");
        else System.out.print(result);
    }
}
