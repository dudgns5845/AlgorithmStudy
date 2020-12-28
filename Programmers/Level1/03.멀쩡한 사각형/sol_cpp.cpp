using namespace std;

//최대 공배수를 구하는 GCD함수
long long GCD(int a, int b){
    long temp;
    
    while(b != 0){
            temp = a%b;
            a=b;
            b=temp;
    }
    return a;
}

long long solution(int w,int h) {
    long long answer = 1;
    
    //입력값이 1억을 넘는다
    long long W = w;
    long long H = h;
    long long non_block = w+h - GCD(w,h);
    
    return W*H - non_block;
}