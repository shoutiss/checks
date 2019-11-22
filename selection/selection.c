/**
 * Selection Sort
 * Fill out the skeleton below to implement a selection sort
 * Your sort must "select" smallest values and sort the list from left to right
 * Pay attention to the places where you must enter code - don't change anything that was
 * already present!
 *
 * Checking for correctness
 * 1. To compile, type: make sort
 * 2. Test by running ./sort
 * 3. When you are done entering items, hit ctrl d
 * 2. Check50: check50 shoutiss/checks/master/selection
 */

#include <cs50.h>
#include <stdio.h>
#include "selection.h"


// Implements a selection sort on an array of values
void selection(int values[], int n)
{
     // Iterate through array n times
    for (int i = 0; i < n - 1; i++)
    {
        // TODO: Implement sorting algorithm


        // Prints the current step of your sorting
        // This must stay in the for loop that begins on line 24.
        // Also ensure that this line does not end up in any loops you create for your sorting...
        print_array(values, n);
    }
    return;
}


// Prints the values of an integer array separated by spaces
void print_array(int values[], int n)
{
    for (int i = 0; i < n - 1; i++)
    {
        printf("%i ", values[i]);
    }
    printf("%i\n", values[n-1]);
}