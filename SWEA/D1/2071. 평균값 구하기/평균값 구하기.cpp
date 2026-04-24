#include <iostream>
#include<cmath>
using namespace std;

int main(){
    int T;
    cin >> T;
    
    for(int tc = 1 ; tc <= T ; tc++){
        int result = 0;
        for(int i = 0 ; i < 10 ; i++){
            int tmp;
            cin >> tmp;
            result += tmp;
        }
        
        cout << "#" << tc << " " << round(result / 10.0) << endl;
    }
    
    return 0;
}