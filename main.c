/*Write a program that outputs 100 lines, numbered 1 to 100, each with your name on it.*/
#include <stdio.h>
int main()
{
    int my_name;
    for(my_name=0; my_name<=100; my_name++)
    {
        printf("%d", my_name);
        printf(". Mori Keli.\n");
        /*The following printf statement will also work:

         * printf("%d. Mori Keli", my_name);

         */
    }
    return 0;
}
