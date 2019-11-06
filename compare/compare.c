/*
 * compare.c
 * Use functions to test which is larger, n! or 5 ^ n
 * Checking: check50 shoutiss/checks/master/compare
 */

#include <stdio.h>
#include <cs50.h>

// Function prototypes - dont change these
int factorial(int n);
int exponent(int n);

// DON'T CHANGE ANYTHING IN MAIN FUNCTION
int main(void)
{
    // Ask user for an integer
    int num = get_int("Integer: ");

    if (factorial(num) > exponent(num))
    {
        printf("%i! is larger.\n", num);
    }
    else
    {
        printf("5 to the %i is larger.\n", num);
    }
}

// YOUR CODE GOES BELOW:
// Write two functions based on the prototypes declared in lines 7 and 8 that perform the expected operations
