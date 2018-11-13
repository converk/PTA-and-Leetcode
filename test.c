#include <stdio.h>

int main()
{
    int now=2000, next=2000, sub_time=-40;
    int result;
    int mod;
    //scanf("%d %d", &now, &sub_time);
    next = now;
    result = sub_time / 60;
    next += result * 100;
    mod = sub_time - result * 60;
    next += mod;
    if ((next - (next / 100) * 100) >= 60)
        printf("%d", next + 40);
    else
        printf("%d", next);
    return 0;
}