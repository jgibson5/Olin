/* Functions for counting cards in blackjack.
 * 
 * Joe Gibson
 * Software Systems
 * Olin College
 * Aug. 30, 2012
 */

#include <stdio.h>
#include <stdlib.h>

/* Prompts user for input and reads response.
 * 
 * Truncates string to 2 characters and returns.
 * 
 * card_name: buffer for storing response
 */
void get_input(char card_name[3])
{
  puts("enter the card_name: ");
  scanf("%2s", card_name);
}

/* Parses card value into count value.
 * 
 * card_name: buffer used to store card value
 */
int parse_val(char card_name[3])
{
  int val = 0;
  switch(card_name[0]) {
  case 'K':
  case 'Q':
  case 'J':
    val = 10;
    break;
  case 'A':
    val = 11;
    break;
  case 'X':
    break;
  default:
    val = atoi(card_name);
    if ((val < 1) || (val > 10)) {
      puts("I don't undertand that value!");
      break;
    }
  }
  return val;
}

/* Runs the while loop to keep updated card count.
 * Prints updated count after each loop.
 * Calls get_input and parse_val inside loop.
 */
int main()
{
  int count = 0;
  char card_name[3];
  int val;
  while (card_name[0] != 'X') {
    get_input(card_name);
    val = parse_val(card_name);
    if ((val > 2) && (val < 7)) {
      count++;
    } else if (val == 10) {
      count--;
    }
    printf("Current count: %i\n", count);
  }
  return 0;
}

