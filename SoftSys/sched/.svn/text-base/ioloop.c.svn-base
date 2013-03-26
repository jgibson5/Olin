/* Example code for Software Systems at Olin College.

Copyright 2012 Allen Downey
License: Creative Commons Attribution-ShareAlike 3.0

*/

#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>

#define FILE_FLAGS (O_WRONLY | O_CREAT | O_TRUNC)
#define FILE_MODE (S_IRUSR | S_IWUSR | S_IRGRP | S_IROTH)


int main (int argc, char *argv[])
{
    int i = 0;
    int iterations;
    int fd;
    int n;
    char buf[] = "a";

    if (argc == 2) {
	iterations = atoi (argv[1]);
    } else {
	printf("Usage: ioloop [iterations]\n");
	exit(-1);
    }

    fd = open ("temp", FILE_FLAGS, FILE_MODE);

    for (i=0; i<iterations/70; i++) {
	n = write(fd, buf, 1);
	if (n != 1) {
	    perror("write failed");
	}
	n = fsync(fd);
	if (n != 0) {
	    perror("fsync failed");
	}
    } 
    close(fd);
    exit(EXIT_SUCCESS);
}
