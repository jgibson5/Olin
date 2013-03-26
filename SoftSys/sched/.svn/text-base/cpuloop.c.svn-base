/* Example code for Software Systems at Olin College.

Copyright 2012 Allen Downey
License: Creative Commons Attribution-ShareAlike 3.0

*/

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <math.h>

int main (int argc, char *argv[])
{
    int i = 0;
    int iterations;
    double x;

    if (argc == 2) {
	iterations = atoi (argv[1]);
    } else {
	printf("Usage: cpuloop [iterations]\n");
	exit(-1);
    }

    for (i=0; i<iterations*22500; i++) {
	x = cos((double) i);
    }
    printf("%f\n", x);
    exit(EXIT_SUCCESS);
}
