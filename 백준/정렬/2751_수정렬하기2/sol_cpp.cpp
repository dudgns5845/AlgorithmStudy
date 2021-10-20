#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

bool compare(int a, int b){
    return a < b;
}

int main(){

    int N;
    cin>> N;
    vector<int> input_list;
    for(int i = 0 ; i < N ; i++){
        int input;
        cin >> input;
        input_list.push_back(input);
    }

    sort(input_list.begin(),input_list.end(),compare);

    for(int i = 0 ; i < N ; i++){
        cout << input_list[i]<<'\n';
    }

    return 0;
}