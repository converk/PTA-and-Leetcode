#include<stdio.h>

int main(void){
    int input_cm;
    int foot,inch;
    scanf("%d",&input_cm);
    foot=input_cm/30.48;
    inch = (input_cm / 30.48 - foot) * 12; //这里的input_cm / 30.48不能变成foot
    printf("%d %d",foot,inch);
    return 0;
}
