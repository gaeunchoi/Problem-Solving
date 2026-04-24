#include <iostream>
using namespace std;

int main(){
    int N;
    cin >> N;
    
    int val = 1;
    for(int i = 0 ; i <= N ; i++){
        cout << val << " ";
        val *= 2;
    }
    return 0;
}