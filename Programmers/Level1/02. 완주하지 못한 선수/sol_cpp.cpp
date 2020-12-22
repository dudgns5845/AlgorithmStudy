#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    
    //파이썬이 다양한 함수를 제공한다는 점에서 좋긴 좋은거 같다.
    sort(participant.begin(),participant.end());
    sort(completion.begin(),completion.end());
    
    for(int i = 0; i<completion.size();i++)
    {
        if(participant[i]!=completion[i])
            return participant[i];
    }
    
    return participant[participant.size()-1];
}