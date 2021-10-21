#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main()
{

    string input_text;
    cin >> input_text;

   for(int i = 0 ; i<input_text.size()/2;i++){
       if(input_text[i] == input_text[input_text.size() -1 -i]){
           continue;
       }else{
           cout<<0;
           return 0;
       }
   }
   cout<<1;
   return 0;
}