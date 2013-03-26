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
    int seconds;
    double x;

    if (argc == 2) {
	seconds = atoi(argv[1]);
    } else {
	printf("Usage: alarm [duration in seconds]\n");
	exit(-1);
    }

    alarm(seconds);
    
    while (1) {
	i++;
	x = cos((double) i);
    }
    printf("%f\n", x);
}
