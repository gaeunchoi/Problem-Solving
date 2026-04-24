#include <iostream>
using namespace std;

int main(){
    int N;
    cin >> N;
    
    int result = 0;
    while(N > 0){
        result += N % 10;
        N /= 10;
    }
     
    cout << result << endl;
    return 0;
}