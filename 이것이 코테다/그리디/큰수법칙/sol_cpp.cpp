#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    int N,M,K;
    int result = 0;
    int first;
    int second;
    scanf("%d %d %d",&N,&M,&K);
    vector<int> list;
    for(int i = 0; i<N;i++){
        int temp;
        scanf("%d",&temp);
        list.push_back(list);
    }

    //최댓값을 찾기 위해서 정렬하기
    list.sort();

    //끝에서 첫번째와 두번째를 저장
    first = list[N-1];
    second = list[N-2];

    while(true){
        for(int i = 0 ; i<K ; i++){
            if (M == 0){
            break;
            }
            result += first;
            M -=1;
        }
        
        if(M==0){
            break;
        }
        result += second;
        M -= 1;
    }

    printf("%d",result);

    return 0;
}
