#include <string>
#include <vector>
#include <queue> //큐를 사용하기 위해서는 queue해더 파일을 include할 것

using namespace std;

int solution(vector<int> scoville, int K) {
    int answer = 0;
    int num1, num2;


    //우선 정렬 큐
    priority_queue<int, vector<int>, greater<int>> temp;
    //우선 정렬 큐는 새로운 값 입력시 정렬을 자동으로 해준다는 장점이 있다.
    for (int i = 0; i < scoville.size(); i++) {
        temp.push(scoville[i]);
    }

    //음식이 2개 이상이고, top(최소 매운 음식)이 K보다 작을 때 실시
    while ( temp.size() > 1 && temp.top()<K) {
        int first, second;
        
        first = temp.top();
        temp.pop();
        second = temp.top();
        temp.pop();

        int spicy = first + second * 2;

        temp.push(first + second * 2);
        answer++;
    }

    if (temp.top() < K) return -1;
 
    return answer;
}