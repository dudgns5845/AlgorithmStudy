#include <iostream>
#include <string>
using namespace std;

int main()
{
    //char alpha [] = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
    int visit[26] = {
        0,
    };

    int word_size;
    //조건을 만족하는 단어 개수
    int word_count = 0;

    //단어 개수 입력
    cin >> word_size;

    for (int i = 0; i < word_size; i++)
    {
        //visit초기화
        for (int j = 0; j < 26; j++)
        {
            visit[j] = 0;
        }

        bool isOkay = true;
        string input_word;
        cin >> input_word;
        char temp = ' ';
        //문자를 하나씩 접근한다
        for (int j = 0; j < input_word.length(); j++)
        {
            //같으면 진행
            if (temp == input_word[j])
            {
                continue;
            }
            //다르면
            else if (temp != input_word[j])
            {
                //방문 했다
                if (visit[(int)input_word[j] - 97] != 0)
                {
                    //cout << "방문했다" << endl;
                    //다음 단어로 넘어감
                    isOkay = false;
                    break;
                }
                //방문 안했다
                else if (visit[(int)input_word[j] - 97] == 0)
                {
                    //cout << "방문안했다" << endl;
                    visit[(int)input_word[j] - 97] = 1; //방문 표시하고
                    temp = input_word[j];               //temp에 할당
                }
            }
        }
        if (isOkay == true)
        {
            word_count++;
        }
    }
    cout << word_count;
    return 0;
}