#include <iostream>
using namespace std;

int main(){
    int T;
    cin >> T;
    
    for(int tc = 1 ;  tc <= T ; tc++){
        int result = -1;
        int tmp;
        for(int i = 0 ; i < 10 ; i ++){
            cin >> tmp;
            if(result < tmp) result = tmp;
        }
        cout << "#" << tc << " " << result << endl;
    }
    return 0;
}