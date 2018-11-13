#include<stdio.h>

int main(void){
    int first,second,third;
    int num;
    scanf("%d", &num);
    first=num/100;
    second=(num-first*100)/10;
    third = num - first * 100-second*10;
    printf("%d", 100*third+10*second+first);
    return 0;
}