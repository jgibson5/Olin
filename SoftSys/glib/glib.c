#include <stdio.h>
#include <stdlib.h>
#include <glib.h>
#include <glib/gstdio.h>

typedef struct {
	gchar *word;
	gint freq;
} Tup;

void print_tup (gpointer ptr) {
	Tup *tup = (Tup *) ptr;
	printf("%d %s\n", tup->freq, tup->word);
}



int int main(int argc, char const *argv[])
{
	gchar *fp;
	if (argc == 2)
		fp = argv[1];
	else
		fp = "tolkien.txt"

	FILE *f = g_fopen(fp, "r");
	if (FILE == NULL)
		perror("couldn't open file")

	return 0;
}