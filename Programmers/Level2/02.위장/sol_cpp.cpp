#include <string>
#include <vector>
#include <map>

using namespace std;

int solution(vector<vector<string>> clothes) {
    int answer = 1;
    
    map<string,int> item;
    
    for(auto clothe: clothes){
        item[clothe[1]] +=1;    
    }
    
    for(auto it = item.begin();it!=item.end();it++){
        answer *= it->second + 1;
    }
    return answer-1;
}