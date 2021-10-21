#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main(){
    int N,M;

    cin >> N >> M;

    vector <string> input_list;
    vector <string> result_list;

    for(int i = 0 ; i < N ; i++){
        string name;
        cin>>name;
        input_list.push_back(name);
    }

    for(int i = 0 ; i< M ; i++){
        string name;
        cin>>name;
        auto it = find(input_list.begin(),input_list.end(),name);
        if(it == input_list.end()){
            result_list.push_back(name);
        }
    }

    cout<< result_list.size()<<'\n';

   for(int i = 0 ; i< result_list.size();i++){
       cout<<result_list[i]<<'\n';
   }

    return 0;
}