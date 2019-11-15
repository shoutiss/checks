// Helper functions

#include <cs50.h>
#include <stdio.h>

#include "bubble.h"


// Implements a bubble sort on an array of values
void bubble(int values[], int n)
{
     // Iterate through array n times
    for (int i = 0; i < n; i++)
    {
        bool swapped = false;
        // Compare adjacent values
        for (int j = 1; j < n - i; j++)
        {
            // If left is larger, swap the values
            if (values[j - 1] > values[j])
            {
                int temp = values[j - 1];
                values[j - 1] = values[j];
                values[j] = temp;
                swapped = true;
            }
        }
        print_array(values, n);

        // No swaps means we're done
        if (!swapped)
        {
            return;
        }
    }
    return;
}

void print_array(int values[], int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("%i\n", values[i]);
    }
}