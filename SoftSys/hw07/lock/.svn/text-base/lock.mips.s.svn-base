	.verstamp	3 19
	.option	pic2
	.text	
	.align	2
	.file	2 "lock.c"
	.globl	acquire
	.loc	2 5
 #   1	#include <stdio.h>
 #   2	#include "lock.h"
 #   3	
 #   4	void acquire (Lock *lock)
 #   5	{
	.ent	acquire 2
acquire:
	.option	O1
	.set	 noreorder
	.cpload	$25
	.set	 reorder
	.frame	$sp, 0, $31
	.loc	2 5
	.loc	2 6

$32:
	ll	$15, 0($4)
	li	$24, 1
	sc	$24, 0($4)
	beq	$24, 0, $32
	beq	$15, 1, $32

$33:
	.loc	2 7
	.loc	2 8
 #   8	}
	.livereg	0x0000FF0E,0x00000FFF
	j	$31
	.end	acquire
	.text	
	.align	2
	.file	2 "lock.c"
	.globl	release
	.loc	2 11
 #   9	
 #  10	void release (Lock *lock)
 #  11	{
	.ent	release 2
release:
	.option	O1
	.set	 noreorder
	.cpload	$25
	.set	 reorder
	.frame	$sp, 0, $31
	.loc	2 11
	.loc	2 12
 #  12	  lock->value = 0;
	sw	$0, 0($4)
	.loc	2 13
 #  13	}
	.livereg	0x0000FF0E,0x00000FFF
	j	$31
	.end	release
