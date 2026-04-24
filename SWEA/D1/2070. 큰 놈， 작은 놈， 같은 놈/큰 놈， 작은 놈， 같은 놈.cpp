#include <iostream>
using namespace std;

int main(){
    int T;
    cin >> T;
    
    for(int tc = 1; tc <= T ; tc++){
        char result;
        int a, b;
        cin >> a >> b;
        
        if(a < b) result = '<';
        else if(a == b) result = '=';
        else result = '>';
        
        cout << "#" << tc << " " << result << endl;
    }
    
    return 0;
}
            