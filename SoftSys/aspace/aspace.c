/* Example code for Software Systems at Olin College.

Copyright 2012 Allen Downey
License: Creative Commons Attribution-ShareAlike 3.0

*/

#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int num, den;
} Rational;

int global;

void recurse (int n)
{
    int a[4000];
    Rational *rv = (Rational *) malloc (1000 * sizeof (Rational));

    printf ("Address of a is %p\n", &a[0]);
    printf ("Address of rv is %p\n", rv);

    if (n > 0) recurse (n-1);
}

int main ()
{
    int local = 5;
    Rational *r1 = (Rational *) malloc (sizeof (Rational));

    printf ("Address of local is %p\n", &local);
    printf ("Address of global is %p\n", &global);
    printf ("Address of main is %p\n", main);
    printf ("Address of r1 is %p\n", r1);
    
    recurse (1);
    return 0;
}
