#include <stdio.h>
 
int main() 
{
    long long int a, b, c, i;
    scanf("%lld %lld %lld", &a, &b, &c);
    for(i = 1 ; i < c; i++)
    {
        a *= b;
    }
     
    printf("%lld", a);
}
