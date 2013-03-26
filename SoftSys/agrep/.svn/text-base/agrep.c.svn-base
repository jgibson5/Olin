/* Joe Gibson
 * Software Systems
 * Olin College
 * 
 * agrep
 * 
 * takes in multiple regex patters through argv and applies them
 * to the input in stdin
 */
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <regex.h>

#define BUF_SIZE 1024

int search(char *input, int argc, char *argv[])
/* applies the regex pattern in argv[argc] to input
 * 
 * returns:
 * 	0 if no match
 *  -1 if error
 *  1 if matched the last regex pattern
 *  calls search again, decrementing the argc input otherwise
 */
{
	regex_t re;
	int r;
	if (argc == 0)
	{
		return 1;
	}
	
	regcomp(&re, argv[argc], 0);
	argc--;
	r = regexec(&re, input, 0, NULL, 0);
	if( !r ){
        return search(input, argc, argv);
    }
    else if( r == REG_NOMATCH ){
        return 0;
    }
	return -1;
}

int main(int argc, char *argv[])
/* reads from stdin and executes the search function for 
 * each line in stdin
 * 
 * sends the parameters in argv to search as regex patterns
 */
{
	char buffer[BUF_SIZE];
	fgets(buffer, BUF_SIZE, stdin);
	while (fgets(buffer, sizeof buffer, stdin))
	{
		if (search(buffer, argc-1, argv))
		{
			printf("%s\n", buffer);
		}
	}
	return 0;
} 