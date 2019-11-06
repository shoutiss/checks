/*
 * triangle.c by Mr. Shoutis
 * Collect 3 integers from a user and test to see if they make a triangle
 *
 * Checking: check50 shoutiss/checks/master/triangle
 *
 */

#include <cs50.h>
#include <stdio.h>

// Add something here - what's missing?

int main(void)
{
    // Collect sides from user
    int side1 = get_int("Enter the first side: ");
    int side2 = get_int("Enter the second side: ");
    int side3 = get_int("Enter the third side: ");

    // COMPLETE THIS MAIN FUNCTION - Print YES\n if the sides could make a triangle
    // print NO\n if the sides cannot make a traingle.
    // you MUST use the function triangle_check

    return 0;
}

bool triangle_check(int a, int b, int c)
{
    if (a < 0 || b < 0 || c < 0)
    {
        return false;
    }

    if ( a + b <= c || a + c <= b || b + c <= a)
    {
        return false;
    }

    return true;
}