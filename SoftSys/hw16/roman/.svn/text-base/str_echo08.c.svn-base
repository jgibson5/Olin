#include	"unp.h"

int roman_to_num(char* roman)
{
	//char accepted = ['I', 'X', 'L', 'V', 'M', 'C', 'D'];
	int total = 0;
	int i = 0;
	//printf("%s\n", roman);
	while (roman[i]) {
		switch (roman[i]) {
		case 'I':
			//printf("I\n%d\n", total);
			total += 1;
			break;
		case 'V':
			//printf("V\n%d\n", total);
			total += 5;
			break;
		case 'X':
			//printf("S\n%d\n", total);
			total += 10;
			break;
		case 'L':
			//printf("L\n%d\n", total);
			total += 50;
			break;
		case 'C':
			//printf("C\n%d\n", total);
			total += 100;
			break;
		case 'D':
			//printf("D\n%d\n", total);
			total += 500;
			break;
		case 'M':
			//printf("M\n%d\n", total);
			total += 1000;
			break;
		default:
			//printf("bad input\n");
			break;
		}
		i++;
	}
	//printf("%d\n", total);

	return total;
}

void
str_echo(int sockfd)
{
	char		arg[16];
	int	 		out;
	ssize_t		n;
	char		line[MAXLINE];

	printf("here\n");
	for ( ; ; ) {
		if ( (n = Readline(sockfd, line, MAXLINE)) == 0)
			return;		/* connection closed by other end */

		if (sscanf(line, "GET /%s http/1.1\n", arg) == 1) {
			printf("1 %s\n%s\n", line, arg);
			out = roman_to_num(arg);
			snprintf(line, sizeof(line), "HTTP/1.0 200 OK\nServer: Apache\n\n<html>%d</html>\n", out);
			n = strlen(line);
			Writen(sockfd, line, n);
			Close(sockfd);
		} else
			printf("not valid\n");
			//snprintf(line, sizeof(line), "not valid\n");

		
	}
}
