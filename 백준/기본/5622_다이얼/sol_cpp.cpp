#include<iostream>
using namespace std;

int main(){
    char alpha [] = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'};
    unsigned time [] = {3, 3, 3, 4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,8,9,9,9,10,10,10,10};
    string input_text;
    int total_time = 0;
    cin>>input_text;
    for(int i = 0 ; i< input_text.length();i++){
        for(int j = 0 ; j < 26;j++){
            if(input_text[i] == alpha[j]){
                total_time += time[j];
            }
        }
    }
    cout<< total_time;
    return 0;
}