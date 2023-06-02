/*DO NOT CHANGE ANYTING IN THIS FILE
 * Usage: ./islandmain
 * Execute this file to see 4 example arrays.
 * You will have to use 4 different inputs to see them (-1, -2, -3, -4)
 * You can use these arrays to plan and test your program.
 * For checking: check50 kanchankant/checks/master/island
 * For submitting: submit50 kanchankant/checks/master/island
 *
 * DO NOT CHANGE ANYTING IN THIS FILE
 */

#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>

#include "island.h"

int main(int argc, string argv[])
{
    // Make sure command line arg exists
    if (argc != 2)
    {
        return 1;
    }

    // Determine test to run
    int test = atoi(argv[1]);

    // Testing Islands
    // expt 24
    int island1[5][5] = {{1,1,1,1,1},{1,1,1,1,0},{1,1,1,1,1},{0,1,1,1,1},{1,1,1,1,1}};
    // 28
    int island2[5][5] = {{1,0,0,1,1},{1,0,1,1,1},{1,0,1,1,0},{1,1,1,0,0},{0,0,1,1,0}};
    // 18
    int island3[5][5] = {{0,0,0,0,0},{1,1,1,1,1},{1,1,1,1,1},{1,1,1,1,1},{1,1,1,1,1}};
    // 36
    int island4[5][5] = {{1,0,1,0,1},{1,0,1,0,1},{1,0,1,0,1},{1,0,1,0,1},{1,1,1,1,1}};

    //int island5[6][6] = {{1, 1, 1, 1, 1, 1}, {1,1,1,1,1,1},{1,1,1,1,1,1},{1,1,1,0,1,1},{1,1,1,1,1,1},{1,1,1,1,1,1}};

    switch (test)
    {
        case 0:
        {
            int perim = mapping(island1);
            printf("%i\n", perim);
            break;
        }

        case 1:
        {
            int perim = mapping(island2);
            printf("%i\n", perim);
            break;
        }
        case 2:
        {
            int perim = mapping(island3);
            printf("%i\n", perim);
            break;
        }
        case 3:
        {
            int perim = mapping(island4);
            printf("%i\n", perim);
            break;
        }
        // case 4:
        // {
        //     int perim = mapping(island5);
        //     printf("%i\n", perim);
        //     break;
        // }
    }




}