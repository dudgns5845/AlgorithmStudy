#include <iostream>
#include <string>

using namespace std;

int main(){

    int h ;
    int count = 0;

    scanf("%d",&h);

    for (int i = 0 ; i < h ; i ++){
        for(int j = 0 ; j < 60; j++){
            for(int k = 0 ; k < 60; k++){
                string temp;
                temp.append(to_string(i));
                temp.append(to_string(j));
                temp.append(to_string(k));
                if(temp.find('3') > 0){
                    count++;
                    break;
                }
            }
        }
    }
    

    /*to_string(num) : num to string 
        숫자 변수를 문자열로 변환시켜주는 메소드
    */

   /*string 메소드
        append(str) : 문자열을 뒤에 추가함
        find(str) : 문자열에 해당 문자열이 몇개 있는지 개수를 반환
   */

    printf("%d",count);

    return 0;
}