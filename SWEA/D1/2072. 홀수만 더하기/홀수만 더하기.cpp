#include<iostream>

using namespace std;

int main(int argc, char** argv)
{
	int T;
	cin>>T;
    
	for(int test_case = 1; test_case <= T; ++test_case)
	{
        int result = 0;
        int tmp;
        for(int i = 0; i < 10; i++) {
            cin >> tmp;
            if(tmp % 2 == 1) result += tmp;
        }
        
        std::cout << "#" << test_case << " " << result << std::endl;
	}
	return 0;
}