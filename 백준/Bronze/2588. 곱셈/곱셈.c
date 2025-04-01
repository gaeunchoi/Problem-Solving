#include <stdio.h>

int main(){
    int a, b;
    scanf("%d %d", &a, &b);
    int b1 = b/100;
    int b2 = b/10 - b1*10;
    int b3 = b%10;
    
    printf("%d\n%d\n%d\n%d", a*b3, a*b2, a*b1, a*b);
}