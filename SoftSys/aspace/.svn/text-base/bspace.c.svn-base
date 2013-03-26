/* Example code for Software Systems at Olin College.

Copyright 2012 Allen Downey
License: Creative Commons Attribution-ShareAlike 3.0

*/

#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>

typedef struct {
    int num, den;
} Rational;

int global;

void recurse (int n, int rec)
{
    int a[4000];
    Rational *rv = (Rational *) malloc (1000 * sizeof (Rational));
    if (rec == 0)
      {
	printf ("Address of a is %p\n", &a[0]);
	printf ("Address of rv is %p\n", rv);
      }
    else
      {
	printf ("Address of threada is %p\n", &a[0]);
	printf ("Address of threadrv is %p\n", rv);
      }
    if (n > 0) recurse (n-1,rec);
}

static void *child(void *ignored)
{
  recurse(1,1);
  return NULL;
}

int main ()
{
    pthread_t child_thread;
    int code;
    int local = 5;
    Rational *r1 = (Rational *) malloc (sizeof (Rational));

    printf ("Address of local is %p\n", &local);
    printf ("Address of global is %p\n", &global);
    printf ("Address of main is %p\n", main);
    printf ("Address of r1 is %p\n", r1);

    code = pthread_create(&child_thread, NULL, child, NULL);
    if (code) {
	fprintf(stderr, "pthread_create failed with code %d\n", code);
    }


    
    recurse (1,0);
    sleep(5);
    return 0;
}
