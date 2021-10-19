#include<iostream>
#include<list>
using namespace std;

int main() {

    //테스트 케이스 개수
    int T;
    cin >> T;

    for (int i = 0; i < T; i++) {
        //괄호 입력 받기
        string input_text;
        cin >> input_text;
        list <char> text_list;

        //문자열이 홀수면 일단 에러
        if (input_text.length() % 2 != 0) {
            cout << "NO" << endl;
            continue;
        }

        //탐색 시작
        for (int j = 0; j < input_text.length(); j++) {
            //stack이 비어있을때
            if (text_list.empty()) {
                if (input_text[j] == '(') {
                    //stack에 삽입
                    text_list.push_back(input_text[j]);
                }
                //비었을때 )이 들어오게 되면 잘 못된 케이스
                else if (input_text[j] == ')') {
                    text_list.push_back(input_text[j]);
                    break;
                }
            }

            //stack이 안비었을때
            else {
                //stack의 최상단 반환
                char temp = text_list.back();
                //case1 stack ( input (
                if (input_text[j] == temp) {
                    //stack에 추가
                    text_list.push_back(input_text[j]);
                }
                //case2 stack ( input )
                else if (input_text[j] != temp) {
                    //최상단 요소 제거
                    text_list.pop_back();
                }
            }
        }
        if (!text_list.empty()) {
            cout << "NO" << endl;
        }
        else {
            cout << "YES" << endl;
        }
    }
    return 0;
}