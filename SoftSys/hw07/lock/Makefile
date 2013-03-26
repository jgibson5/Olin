badlock: lock.c main.c
	gcc -Wall main.c lock.c -o badlock

goodlock: lock.x86.s main.c
	gcc -Wall main.c lock.x86.s -o goodlock

example: example.c
	gcc -Wall example.c -o example -lpthread

clean:
	rm -f *~ badlock goodlock example


FILES = Makefile lock.c  lock.mips.s  lock.x86.s \
example.c  lock.h  lock.s       main.c

DEST = /home/downey/public_html/ss12

lock_tgz:
	rm -rf lock
	mkdir lock
	cp $(FILES) lock
	tar -czf lock.tgz lock
	rsync lock.tgz $(DEST)
	cd /home/downey/public_html; sh back
