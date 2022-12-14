// this code doesn't work lol
#include <stdio.h>
int max(int a, int b) {
    if (a > b) {
        return a;
    }
    return b;

}

int main() {
    int maxCal = 0;
    int sum = 0;
    int valid = 1;
    int value = 0;
    while (1) {
        while (valid) {
            sum += value;
            valid = scanf("%d\n", &value);
            
        }
        maxCal = max(maxCal, sum);
        printf("%d\n", sum);
        if(!scanf("%d\n", &value)) {
            break;
        }
        sum = 0;
    }   
    printf("%d\n", maxCal);

}