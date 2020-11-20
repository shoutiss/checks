/*
 * dblletter.c
 * YOUR TASK: Complete the code below so that double letters are removed
 * Example: An input of Halloween -> Halowen
 *
 * Check your work: check50 shoutiss/checks/master/dblletter
 * Submit your work: submit50 shoutiss/checks/master/dblletter
*/

#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // Get name from user:
    string name = get_string("Enter name: ");

    // Print first character
    printf("%c", name[0]);

    // Iterate through string
    for (int i = 0, n = strlen(name); i < n - 1; i++)
    {
        // YOUR CODE HERE
    }
    printf("\n");
}