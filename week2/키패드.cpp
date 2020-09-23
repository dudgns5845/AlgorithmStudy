#include <string>
#include <vector>

using namespace std;

class righthand{
    //좌표를 나타내주는 인덱스
    int position_x;
    int position_y;
public:
    
    righthand(){
        position_x = 3;
        position_y = 0;
    }
    
}

class lefthand{
  //좌표를 나타내주는 인덱스
    int position_x;
    int position_y;
public:
    
    righthand(){
        position_x = 3;
        position_y = 0;
    }
}

string solution(vector<int> numbers, string hand) {
    string answer = "";
    
    int [][] keypad = {
        {1,2,3},
        {4,5,6},
        {7,8,9},
        {10,0,10}
    };
    
    
    for(int i = 0 ; i < numbers.size();i++){
        //1,4,7은 무조건 왼손
        if(numbers[i]==1 || numbers[i] ==4||numbers[i] ==7){
            answer += "L";
            continue;
        }
        //3,6,9는 무조건 오른손
        if(numbers[i]==3 || numbers[i] ==6||numbers[i] ==9){
            answer += "R";
            continue;
        }
        //2,5,8,0의 경우는 조건에 따라서
        else{
            

        }
        
        
        
    }
    
    return answer;
}