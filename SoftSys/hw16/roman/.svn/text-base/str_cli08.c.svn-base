#include	"unp.h"

void
str_cli(FILE *fp, int sockfd)
{
	char	sendline[MAXLINE], recvline[MAXLINE];
	char *	header;
	header = "GET LVM http/1.1\nHost: 127.0.0.1\n\n";

	while (Fgets(sendline, MAXLINE, fp) != NULL) {

		Writen(sockfd, header, strlen(header));

		if (Readline(sockfd, recvline, MAXLINE) == 0)
			err_quit("str_cli: server terminated prematurely");

		Fputs(recvline, stdout);
	}
}
