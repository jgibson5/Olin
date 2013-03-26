
/* Joe Gibson
 * Orion Taylor
 * Software Systems
 * Olin College
 * 
 * HW08
 * 
 * tee - takes input and writes to output file. 
 * writes to stdout by default, or to file in arguments
 * 
 * -a - appends to file instead of overwriting
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>




/* Reads from stdin and writes to output.
 * If no argument, output is stdout.
 * If argument, output is file in argument.
 * 
 * -a - appends to file in argument instead of overwriting file
 */
int main(int argc, char *argv[])
{
	FILE *out_file;
	char ch;
	int flag_a = 0;
	char info[80];
	int count = 0;
	
	
	while ((ch = getopt(argc, argv, "a")) != EOF) {
		switch(ch) {
		case 'a':
			flag_a = 1;
			break;
		argc -= optind;
		argv += optind;
		}
	}
	
	while (fgets(info, sizeof(info), stdin)) {

		if (argc > 1) {
			if (flag_a || count) {
				out_file = fopen(argv[flag_a+1], "a");
			} else {
				out_file = fopen(argv[flag_a+1], "w");
			}
			fprintf(out_file, "%s", info);
			fclose(out_file);
		}
		if (!count) {
			count++;
		}
		printf("%s", info);
	}
	return 0;
}

