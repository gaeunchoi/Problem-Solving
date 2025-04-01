import java.util.*;

class Grade {
    int document;
    int interview;

    public Grade (int document, int interview){
        this.document = document;
        this.interview = interview;
    }

    public int getDocument() {
        return document;
    }

    public int getInterview() {
        return interview;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        for(int i = 0 ; i < t ; i++){
            Vector<Grade> grade = new Vector<Grade>();
            int n = scanner.nextInt();
            for(int j = 0 ; j < n ; j++){
                int docu = scanner.nextInt();
                int inter = scanner.nextInt();
                grade.add(new Grade(docu, inter));
            }

            Collections.sort(grade, new Comparator<Grade>() {
                @Override
                public int compare(Grade o1, Grade o2) {
                    return o1.document - o2.document;
                }
            });

            int cnt = 1;
            Grade start = grade.firstElement();
            for(Grade saram : grade){
                if(saram.getInterview() < start.getInterview()){
                    start = saram;
                    cnt++;
                }
            }

            System.out.println(cnt);
        }
    }
}
