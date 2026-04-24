#include <iostream>
using namespace std;

int main(){
    for(int i = 0 ; i < 5 ; i++){
        string row = "";
        for(int j = 0 ; j < 5; j++){
            if(i == j) row += "#";
            else row += "+";
        }
        cout << row << endl;
    }
    return 0;
}