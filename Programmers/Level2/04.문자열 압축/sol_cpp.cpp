#include <iostream>
#include <string>
#include <vector>
using namespace std;

int solution(string s){

    //입력문자열의 길이값으로 초기화해놓는다.
    //문자열 그대로가 정답일 경우면 그냥 answer을 반환하면 된다.
    int answer = s.length();

    //완전 탐색을 통해서 압축을 진행해보자
    //한글자, 두글자,,, 입력문자의 절반 길이까지 비교 실시한다
    //입력문자의 절반까지만 비교하는 이유는 그 길이를 넘어가면 압축의 의미가 없기 때문이다.
    //우리는 압축의 결과가 중요한게 아니라 최소로 압축된 문자열의 길이만 관심이 있다.
    //따라서 압축의 결과를 저장할 필요없다

    for(int i = 1 ; i <= s.length()/2; i++){
        string convert; //한번 루프를 돌때 나온 압축 결과를 저장하는 곳
        string temp; //비교하기 위해 추출한 문자열을 저장하는 곳 

        int cnt = 1; //추출된 문자열(temp)와 나머지 문자열들과 비교해 일치하는 문자들의 개수를 count하는 변수

        temp = s.substr(0,i); //비교하려는 문자열을 처음에서 i번째까지 추출

        //이 반복문의 과정이 중요한데
        //루프를 한번 돌때마다 인덱스가 j+=i가 된다. 즉 i는 추출된 문자열의 길이와 동일하므로
        //비교를 할때도 인덱스가 i만큼 증가해야한다는 것이다.
        for(int j = i ; j < s.length(); j+=i){
            //temp의 길이만큼 뒤에 문자열을 추출해서 같으면 cnt++
            if(temp == s.substr(j,i)){
                cnt++;
            }
            //그러다가 다른 문자열이 나오게 되면 진행결과를 convert에 저장하고 다시 새로운 temp를 저장하고 비교를 한다
            else{
                
                //convert는 숫자+추출문자열을 저장해나가는 곳
                //조건에서 동일한 문자열이 1개 이상이면 숫자를 적어주고 아니면 문자열만 적는다
                if(cnt>1){
                    convert+= to_string(cnt);
                }
                convert+=temp; //추출한 문자열도 저장해주고
 
                //여기서 다시 문자열을 새로 추출하고 다시 시작!!
                //cnt도 다시 1부터 시작!!
                temp = s.substr(j,i);
                cnt = 1;
                
            }
        }

        //내부의 for문을 하다가 마지막에 비교에서 결과를 convert에 저장하지 못한채 끝나기에.
        //한번 더하면 된다.
        if(cnt>1){convert+= to_string(cnt);}
        convert+=temp;

        //여기까지가 외부 for문이 한번 실행된것이다.
        //한글자부터 문자열/2까지 진행될때마다 convert에는 다른 문자열들이 저장될 것이다.
        //그러나 최종적으로 제일 작은 문자열 길이를 갱신해주면 그게 최종 답이된다.
        if(answer > convert.length()){
            answer = convert.length();
        }
    return answer;
}


