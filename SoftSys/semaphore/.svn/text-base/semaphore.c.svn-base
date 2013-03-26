#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>

// UTILITY CODE

void perror_exit (char *s)
{
  perror (s);

  exit (-1);

}

void *check_malloc(int size)
{
  void *p = malloc (size);
  if (p == NULL) perror_exit ("malloc failed");
  return p;
}

// MUTEX WRAPPER

typedef pthread_mutex_t Mutex;

Mutex *make_mutex ()
{
  Mutex *mutex = check_malloc (sizeof(Mutex));
  int n = pthread_mutex_init (mutex, NULL);
  if (n != 0) perror_exit ("make_lock failed"); 
  return mutex;
}

void mutex_lock (Mutex *mutex)
{
  int n = pthread_mutex_lock (mutex);
  if (n != 0) perror_exit ("lock failed");
}

void mutex_unlock (Mutex *mutex)
{
  int n = pthread_mutex_unlock (mutex);
  if (n != 0) perror_exit ("unlock failed");
}


// conditional variable wrapper

typedef pthread_cond_t Cond;

Cond *make_cond () {
  Cond *cond = check_malloc (sizeof(Cond));
  int n = pthread_cond_init (cond, NULL);
  if (n != 0) perror_exit ("make_cond failed"); 
  return cond;
}

void cond_wait (Cond *cond, Mutex *mutex) {
  if (!pthread_cond_wait(cond, mutex)) perror_exit ("cond_wait failed");
}

void cond_signal (Cond *cond) {
  if (!pthread_cond_signal(cond)) perror_exit ("cond_signal failed");
}


// semaphoressssssssssss

typedef struct {
  int value, wakeups;
  Mutex *mutex;
  Cond *cond;
} Semaphore;

Semaphore *make_semaphore (int value)
{
  Semaphore *semaphore = check_malloc (sizeof(Semaphore));
  semaphore->value = value;
  semaphore->wakeups = 0;
  semaphore->mutex = make_mutex ();
  semaphore->cond = make_cond ();
  return semaphore;
}

/* Increments the semaphore */
void incr_semaphore(Semaphore *semaphore) {
  mutex_lock(semaphore->mutex);
  printf("PLUS-----%d\n", semaphore->value);
  semaphore->value++;
  printf("PLUS-----%d\n", semaphore->value);
  mutex_unlock(semaphore->mutex);
  if (semaphore->value == 1)
    cond_signal(semaphore->cond);
}

/* Decrements the semaphore */
void decr_semaphore(Semaphore *semaphore) {
  mutex_lock(semaphore->mutex);
  printf("MINUS-----%d\n", semaphore->value);
  while (!semaphore->value){
    cond_wait(semaphore->cond, semaphore->mutex);
  }
  semaphore->value--;
  printf("MINUS-----%d\n", semaphore->value);
  mutex_unlock(semaphore->mutex);
}

/* Thread 1 executes this function */
void *thread1 (void *arg) {
  Semaphore *n = (Semaphore *) arg;
  //printf("1------------%d\n", n->value);
  incr_semaphore(n);
  //printf("1------------%d\n", n->value);
  pthread_exit(0);
  return (void *) NULL;
}

/* Thread 2 executes this function */
void *thread2 (void *arg) {
  Semaphore *n = (Semaphore *) arg;
  //printf("2------------%d\n", n->value);
  decr_semaphore(n);
  //printf("2------------%d\n", n->value);
  pthread_exit(0);
  return (void *) NULL;
}

/* Creates two threads that share a semaphore.
 * Tests to see if the semaphore works properly.
 */
int main()
{
  pthread_t pro, con;
  Semaphore *semaphore = make_semaphore(10);
  pthread_create(&pro, NULL, thread1, (void *) semaphore);
  pthread_create(&con, NULL, thread2, (void *) semaphore);
  sleep(1);
  return 0;
}