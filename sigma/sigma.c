/*
 * sigma.c by Mr. Shoutis
 * 10/18/2019
 * add a series of command line arugments
 */

 // Check for correctness: check50 shoutiss/checks/master/sigma

#include <cs50.h>
#include <stdlib.h>
#include <stdio.h>

int main(int argc, string argv[])
{
    // TODO 1: Ensure that there are command line arguments. Return 1 if there aren't enough.

    int sum = 0;

    // TODO 2: Add each of the command line arguments to sum. You may assume the arguments
    // are integers, but remember what data type they come in as...

    printf("%i\n", sum);
    return 0;
}


/* Solution:
int main(int argc, string argv[])
{
    if (argc < 2)
    {
        printf("Usage: ./sigma [INTEGERS]\n");
        return 1;
    }

    int sum = 0;
    for (int i = 0; i < argc; i++)
    {
        sum = sum + atoi(argv[i]);
    }

    printf("%i\n", sum);
    return 0;
}
*/