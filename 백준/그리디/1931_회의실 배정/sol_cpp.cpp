#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    int n;
    cin >> n;
    vector<pair<int,int>> a(n); //미리 할당
    
    //입력받기
    for(int i = 0 ; i < n ; i++){
        cin >> a[i].second >> a[i].first;
    }

    //정렬
    sort(a.begin(), a.end());

    int time = 0, answer = 0;

    //그리디는 뒷부분을 고려하지 않고 현재 상황에서 가장 최적화된 답을 고르는 알고리즘
    for(int i = 0 ; i < n ; i++){
        if(time <= a[i].second){
            time = a[i].first;
            answer++;
        }
    }

    cout<< answer;

    return 0;
}