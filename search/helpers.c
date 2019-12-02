// Helper functions

#include <cs50.h>

#include "helpers.h"

#define MAXVAL 65536

// To Check: check50 shoutiss/checks/master/search

// Perform a binary search for a value
bool search(int value, int values[], int n)
{
    // TODO - return true if value is found in values
    // n is the number of elements in the array values[]
    return false;
}

// Sorts array of n values
void sort(int values[], int n)
{
    // Create storage array
    int sorter[MAXVAL] = {0};
    // Iterate through values and count how many of each
    for (int i = 0; i < n; i++)
    {
        sorter[values[i]] += 1;
    }

    int val_index = 0;
    //  Enter values based on count in sorter array
    for (int i = 0; i < MAXVAL; i++)
    {
        if (sorter[i] > 0)
        {
            for (int j = 0; j < sorter[i]; j++)
            {
                values[val_index] = i;
                val_index += 1;
            }
        }
    }
    return;
}
