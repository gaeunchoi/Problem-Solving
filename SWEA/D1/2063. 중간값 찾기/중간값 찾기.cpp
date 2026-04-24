#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    int N;
    cin >> N;
    int nums[N];
    
    for(int i = 0 ; i < N ; i++){
        cin >> nums[i];
    }
    
    sort(nums, nums+N);
    cout << nums[N / 2] << endl;
    
    return 0;
}