#include <iostream>
#include <functional>
#include <queue>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    
    priority_queue<int> max_heap;
    priority_queue<int, vector<int>, greater<int>> min_heap;

    int n;
    cin >> n;
    
    int x;

    for (int i = 0; i < n; i++)
    {
        cin >> x;

        //맨 처음 값
        if (max_heap.size() == 0)
        {
            max_heap.push(x);
        }
        else
        {
            //최대 힙의 개수가 최소 힙의 개수보다 크면 원소를 최소 힙에 넣는다
            if (max_heap.size() > min_heap.size())
            {
                min_heap.push(x);
            }
            else
            {
                max_heap.push(x);
            }
            //만약 최대 힙의 top(중간값)이 최소 힙의 top보다 크면 서로 바꿔줘야한다.
            if (max_heap.top() > min_heap.top())
            {
                int max_temp = max_heap.top();
                int min_temp = min_heap.top(); 
                max_heap.pop();
                min_heap.pop();
                max_heap.push(min_temp);
                min_heap.push(max_temp);
            }
        }
        cout << max_heap.top()<<'\n';
    }
    return 0;
}