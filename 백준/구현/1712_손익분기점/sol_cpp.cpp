#include<iostream>
using namespace std;

int main(){
    
    int A,B,C;
    int breakPoint = 0;
    
    cin >> A >> B >> C;

    if(B>=C){
        cout<< -1;
        return 0;
    }

    cout<<A/(C-B) + 1;

    return 0;
}