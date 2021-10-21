#include<iostream>
using namespace std;

int main()
{
    int alpha[26]  = {
        0,
    };

    string input_text;

    cin >> input_text;

    for(int i = 0 ; i < input_text.size();i++){
        alpha[(int)input_text[i]-97] ++;
    }

    for(int i = 0 ; i < 26;i++){
        cout << alpha[i] << " ";
    }

    return 0;
}