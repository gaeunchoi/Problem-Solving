#include <iostream>
#include <string>
using namespace std;

int main(){
    int T;
    cin >> T;
    int days[13] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    
    for(int tc = 1 ; tc <= T ; tc++){
        string date;
        cin >> date;
        
        int y = stoi(date.substr(0, 4));
        int m = stoi(date.substr(4, 2));
        int d = stoi(date.substr(6, 2));
        
        string result;
        if(1 <= m && m <= 12 && 1 <= d && d <= days[m]) result = date.substr(0, 4) + "/" + date.substr(4, 2) + "/" + date.substr(6, 2);
        else result = "-1";
        
        cout << "#" << tc << " " << result << endl;
    }
    return 0;
}