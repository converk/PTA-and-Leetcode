#include<stdio.h>

int next_time(int, int);

int main(){
    int now,sub_time;
    scanf("%d %d", &now, &sub_time);
    if(sub_time>=0){
        printf("%d", next_time(now,sub_time));
    }else{
        int i;
        for (i=0;i*60+sub_time<0;i++);
        printf("%d", next_time(now,i*60+sub_time)-i*100);
    }  
    return 0;
}

int next_time(int now, int sub_time){
    int result;
    int mod;
    int next;
    next = now;
    result = sub_time / 60;
    next += result * 100;
    mod = sub_time - result * 60;
    next += mod;
    if ((next - (next / 100) * 100) >= 60)
        return next+40;
    else
        return next;
}