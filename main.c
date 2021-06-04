/*Write a program that asks the user for a year and prints whether it is a leap year or not.*/
#include <stdio.h>

int main()
{
    int yr;
    printf("Enter a year: ");
    scanf("%d", & yr);

    if (yr%4==0 && yr%100!=0)
    {
        printf("%d is a leap year.", yr);
    }
    else if (yr%100==0 && yr%400==0)
    {
        printf("%d", yr);
        printf(" yr is  a leap yr");
    }
    else {
        printf("%d", yr);
        printf(" is not a leap year.");
    }
    return 0;
}