#include <string>
#include <vector>
#include <queue>
#include <iostream>
using namespace std;

int solution(int bridge_length, int weight, vector<int> truck_weights)
{
    int answer = 0;

    queue<int> que;

    for (int i = 0; i < bridge_length; i++)
    {
        que.push(0);
    }

    int index = 0;
    int Sum = 0;

    while (!que.empty())
    {
        cout << que.front() << "\n";
        Sum -= que.front();
        que.pop();
        answer++;
        //무게가 같거나 작으면 승차
        if (Sum + truck_weights[index] <= weight)
        {
            que.push(truck_weights[index]);
            Sum += truck_weights[index];
            index++;
        }
        else
        {
            que.push(0);
        }
    }

    return answer;
}

void main(){
    vector<int> test = {7,4,5,6};

    solution(2,10,test);
    
    return;
}
