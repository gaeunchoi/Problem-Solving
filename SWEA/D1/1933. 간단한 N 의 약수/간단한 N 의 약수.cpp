#include <iostream>
using namespace std;

int main(){
    int N;
    cin >> N;
    
    for(int i = 1; i <= N / 2 ; i++)
        if(N % i == 0) cout << i << " ";
    cout << N;
    return 0;
}