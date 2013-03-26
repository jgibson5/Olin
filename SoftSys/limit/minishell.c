/* Joe Gibson
 * Software Systems
 * Olin College
 * 
 * minishell
 * 
 * shell program that limits system resources for the shelled program
 * limits CPU process time to 1 second with the -t flag
 */
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/resource.h>
#include <sys/time.h>



int main(int argc, char **argv)
/* reads the flags for minishell and limits corresponding 
 * system resource using setrlimit
 *
 * -t limits cpu time to 1 second
 * 
 * calls execvp to execute the shelled program
 */
{
	int f;
	while ((f = getopt(argc, argv, "-t:")) != -1){
		switch (f){
			case 't':
				{
				struct rlimit rl;
				getrlimit(RLIMIT_CPU, &rl); 
				printf("\n Default value is : %lld\n", (long long int)rl.rlim_cur); 
    
   				rl.rlim_cur = 1; 

				setrlimit (RLIMIT_CPU, &rl); 
				getrlimit (RLIMIT_CPU, &rl); 
  
   				printf("\n Default value now is : %lld\n", (long long int)rl.rlim_cur); 
   				argc -= 1;
				break;
				}
			default:
				printf("Not a valid flag\n");
				//exit(1);
		}
	}
	argc -= optind;
	argv += optind - 1;

	printf("run %s \n", argv[0]);
	
	execvp(argv[0], argv);
}
