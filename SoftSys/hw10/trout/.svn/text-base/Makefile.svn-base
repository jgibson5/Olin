trout: trout.h trout.c util.c
	gcc -o trout trout.c util.c

main: trout.h util.h main.c trout.c util.c
	gcc -o main main.c trout.c util.c -Wall
