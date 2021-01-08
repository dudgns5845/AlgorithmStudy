#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> prices) {
    vector<int> answer;
    
    //일단 마지막 초까지의 길이 값을 미리 넣어줌
    //[0] = 4, [1] = 3, [2] = 2, [3] = 1, [4] = 0
    for(int i = 0 ; i < prices.size();i++){
        answer.push_back(prices.size()-1-i);
    }
    
    //떨어지는 구간의 값을 카운트 해서 변경해주기
    for(int i = 0 ; i < prices.size()-1; i ++){
        for(int j = i+1 ; j < prices.size();j++){
            if(prices[i]>prices[j]){
                answer[i] = j - i ;
                break;
            }
        }
    }
    
    return answer;
}