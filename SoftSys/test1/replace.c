#include <string.h>

char replace(char *s, char *old, char *new) {
	char *loc = strstr(s, old);
	char *new_s;
	if (loc != NULL) {
		
		int old_len = strlen(old) - 1;
		int new_len = strlen(new) - 1;
		int s_len = strlen(s) - 1;
		
		int new_s_len = s_len - old_len + new_len + 1;
		new_s = malloc (new_len * (sizeof( char)));
	}
	//printf("%p\n", loc);
	return *s;
}

int main() {
	char *s = "test";
	char *old = "old";
	char *new = "new";
	
	
	
	char new_s = replace(s, old, new);
}
