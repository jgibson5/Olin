/* Joe Gibson
 * HW09 Software Systems
 * Olin College
 * 
 * MMU simulation
 * 
 * 
 * Original Copy Info:
 * Example code for Software Systems at Olin College.

Copyright 2012 Allen Downey
License: Creative Commons Attribution-ShareAlike 3.0



*/

#include <stdio.h>
#include <stdlib.h>

#define NUMBER_OF_PAGE_FRAMES 35
#define PAGE_SIZE 1024
#define PHYSICAL_MEMORY_SIZE (NUMBER_OF_PAGE_FRAMES * PAGE_SIZE)

unsigned int page_table[NUMBER_OF_PAGE_FRAMES];
char *physical_memory = NULL;


/* fetch_va: fetches a value from physical memory.
 * 
 * va: long of the virtual memory address
 * 
 * returns the page frame associated with the va
 */
char fetch_va(char *va)
{
  unsigned long pa = (unsigned long) va >> 10;
  int value = page_table[pa];
  return value;
}

void populate_page_table()
{
  int i;
  for (i=0; i<NUMBER_OF_PAGE_FRAMES; i++) {
    page_table[i] = i;
  }
}

void print_page_table()
{
  int i;
  for (i=0; i<NUMBER_OF_PAGE_FRAMES; i++) {
    printf("%d\t%d\n", i, page_table[i]);
  }
}

int main()
{
  physical_memory = (char *) malloc(sizeof(char) * PHYSICAL_MEMORY_SIZE);

  populate_page_table();
  //print_page_table();

  char *va = (char *) 0x0fff;
  char value = fetch_va(va);

  printf("page frame %d\n", value);

  return 0;
}



