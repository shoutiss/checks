/**
 * Bubble Sort
 * Fill out the skeleton below to implement a bubble sort
 * Your sort must "bubble" larger values to the right of the list
 * Pay attention to the places where you must enter code - don't change anything that was
 * already present!
 *
 * Checking for correctness
 * 1. To compile, type: make sort
 * 2. Test by running ./sort
 * 3. When you are done entering items, hit ctrl d
 * 2. Check50: check50 shoutiss/checks/master/bubble
 */

#include <cs50.h>
#include <stdio.h>
#include "bubble.h"


// Implements a bubble sort on an array of values
void bubble(int values[], int n)
{
     // Iterate through array n times
    for (int i = 0; i < n; i++)
    {
        // TODO: Implement sorting algorithm



        // Prints the current step of your sorting
        // This must stay in the for loop that begins on line 22.
        // Also ensure that this line does not end up in any loops you create for your sorting...
        print_array(values, n);

        //TODO: Make sure your algorithm recognizes an already sorted list
    }
    return;
}

void print_array(int values[], int n)
{
    for (int i = 0; i < n - 1; i++)
    {
        printf("%i ", values[i]);
    }
    printf("%i\n", values[n-1]);
}