/* HW2 for Software Systems
 * Olin College
 * Joe Gibson
 * 9-9-12
 *
 * Creates a child thread within a parent thread, printing a unique message
 * loop to each thread. 
 */

#include <pthread.h>
#include <stdio.h>
#include <unistd.h>
#include <time.h>


/* Sleeps for the given number of seconds and nanoseconds.
 *
 * Thread becomes available for scheduling after the given time has
 * elapsed, but may not be scheduled immediately.
 */
void call_nanosleep(long seconds, long nanosecs)
{
    struct timespec requested, remaining;
    requested.tv_sec = seconds;
    requested.tv_nsec = nanosecs;
    nanosleep(&requested, &remaining);
}

/* Prints out a given message a given number of times, sleeping a specified
 * amount between each loop.
 * 
 * count: int number of loop iterations
 * message: char message to print
 * sec: long seconds between each loop
 * nsec: long nano seconds between each loop
 */
void run_loop(int count, char message[],long sec, long nsec)
{
  int c;
  for (c = 0; c < count; c++)
    {
      printf("%s\n", message);
      call_nanosleep(sec, nsec);
    }
}

/* Child thread function- calls run_loop with the child parameters.
 */
static void *child(void *ignored)
{
    run_loop(10, "I'm a child.", 0L, 500000000L);
    return NULL;
}

/* main function that creates the child thread and calls run_loop
 * for the parent thread.
 */
int main(int argc, char *argv[])
{
    pthread_t child_thread;
    int code;

    code = pthread_create(&child_thread, NULL, child, NULL);
    if (code) {
	fprintf(stderr, "pthread_create failed with code %d\n", code);
    }
    run_loop(10, "I'm a parent", 1L, 0L);
    return 0;
}


