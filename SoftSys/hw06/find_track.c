/* Joe Gibson
 * Software Systems
 * Olin College
 * 
 * modified from code example on page 94 of Head First C
 * 
 * Prompts user for regexp pattern and searches list of song names,
 * printing any that match the pattern.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <regex.h>

char tracks[][80] = {
	"I left my heart in Harvard Med School",
	"Newark, Newark - a wonderful town",
	"Dancing with a Dork",
	"From here to maternity",
	"The girl from Iwo Jima"
};

/* http://stackoverflow.com/questions/1085083/regular-expressions-in-c-examples
 * 
 * compiles the regexp pattern from search_for and matches it against
 * the list of song titles, printing any that match
 * 
 * search_for: char array of the regexp pattern from user
 */
void find_track(char search_for[])
{
	int i;
	regex_t re;
    int r;
	
	search_for[strlen(search_for)-1] = '\0';
	regcomp(&re, search_for, 0);

	for (i=0; i<6; i++) {
        if (0 == regexec(&re, tracks[i], 0, NULL, 0)) {
            puts(tracks[i]);
        }
	}
}

/* Prompts user for a regexp pattern, fgets the response, and calls
 * find_track to match it against list of song titles
 */
int main()
{
	char search_for[80];
	printf("Search for: ");
	fgets(search_for, 80, stdin);
	find_track(search_for);
	return 0;
}
