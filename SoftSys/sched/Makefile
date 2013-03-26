alarm: alarm.c
	gcc -Wall -o alarm alarm.c -lm

cpuloop: cpuloop.c
	gcc -Wall -o cpuloop cpuloop.c -lm

ioloop: ioloop.c
	gcc -Wall -o ioloop ioloop.c -lm

FILES = Makefile alarm.c cpuloop.c ioloop.c
DEST = /home/downey/public_html/ss12

sched_tgz:
	rm -rf sched
	mkdir sched
	cp $(FILES) sched
	tar -czf sched.tgz sched
	rsync sched.tgz $(DEST)

