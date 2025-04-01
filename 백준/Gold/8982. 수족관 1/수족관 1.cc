
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

const int MAX = 40000 + 1;

int N, M;
pair<int, int> depth[MAX]; //{해당 column 깊이, 빠져나간 물의 깊이}

int main(void)
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cin >> N;

	int x, y, x2, y2;
	cin >> x >> y; // 처음 0, 0 처리
	for (int i = 0; i < N/2 - 1; i++)
	{
		cin >> x >> y >> x2 >> y2;
		for (int j = x; j < x2; j++)
			depth[j].first = y;
	}
	cin >> x >> y; // 마지막 (x, 0) 처리
	
	int row = x;	
	cin >> M;
	vector<int> hole;
	for (int i = 0; i < M; i++)
	{
		cin >> x >> y >> x2 >> y2;
		//해당 칸만 알면 됨
		hole.push_back(x);
	}
	for (int i = 0; i < hole.size(); i++)
	{
		x = hole[i];
		int height = depth[x].first;
		depth[x].second = height;

		//왼쪽
		for (int j = x - 1; j >= 0; j--)
		{
			//더 이상 깊어질 수 없다
			height = min(height, depth[j].first);
			//최대 깊이만큼 물은 빠진다
			depth[j].second = max(depth[j].second, height);
		}
		height = depth[x].first;
		//오른쪽
		for (int j = x + 1; j < row; j++)
		{
			height = min(height, depth[j].first);
			depth[j].second = max(depth[j].second, height);
		}
	}

	int result = 0;
	//최대 깊이 - 빠져나간 물의 깊이
	for (int i = 0; i < row; i++)
		result += depth[i].first - depth[i].second;
	cout << result << "\n";
	return 0;
}