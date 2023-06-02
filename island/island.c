/*Complete the function below
* This file will not have a main function. DO NOT ADD ONE.
* Type the next 2 commands in your terminal:
* make islandmain
* ./islanmain
* You can use different test islands to see if your function works.
* To use different test islands, give input -1, -2, -3, -4
*/


#include <cs50.h>
#include <stdio.h>

#include "island.h"

int mapping(int island[5][5])
{
    // Variable to hold total perimeter
    int perimeter = 0;

    // Iterate through each island location
    for (int row = 0; row < 5; row++)
    {
        for (int col = 0; col < 5; col++)
        {
            // Search around each piece of land
            if (island[row][col] == 1)
            {
                // Looking up
                if (row == 0)
                {
                    perimeter++;
                }
                else if (island[row - 1][col] == 0)
                {
                    perimeter++;
                }

                // Looking down
                if (row == 4)
                {
                    perimeter++;
                }
                else if (island[row + 1][col] == 0)
                {
                    perimeter++;
                }

                // Looking left
                if (col == 0)
                {
                    perimeter++;
                }
                else if (island[row][col - 1] == 0)
                {
                    perimeter++;
                }

                // Looking right
                if (col == 4)
                {
                    perimeter++;
                }
                else if (island[row][col + 1] == 0)
                {
                    perimeter++;
                }
            }
        }
    }

    // Success!
    return perimeter;
}
