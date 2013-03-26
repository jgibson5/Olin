	.file	"lock.c"
	.version	"01.01"
gcc2_compiled.:
.text
	.align 4
.globl make_lock
	.type	 make_lock,@function
make_lock:
	pushl	%ebp
	movl	%esp, %ebp
	subl	$8, %esp
	subl	$12, %esp
	pushl	$28
	call	malloc
	addl	$16, %esp
	movl	%eax, %eax
	movl	%eax, -4(%ebp)
	movl	-4(%ebp), %eax
	movl	$0, (%eax)
	movl	-4(%ebp), %eax
	movl	%eax, %eax
	leave
	ret
.Lfe1:
	.size	 make_lock,.Lfe1-make_lock
	.align 4
.globl acquire
	.type	 acquire,@function
acquire:
	pushl	%ebp
	movl	%esp, %ebp
	nop
	.p2align 2
.L4:
	movl	8(%ebp), %eax
	cmpl	$1, (%eax)
	je	.L4
	movl	8(%ebp), %eax
	movl	$1, (%eax)
	popl	%ebp
	ret
.Lfe2:
	.size	 acquire,.Lfe2-acquire
	.align 4
.globl release
	.type	 release,@function
release:
	pushl	%ebp
	movl	%esp, %ebp
	movl	8(%ebp), %eax
	movl	$0, (%eax)
	popl	%ebp
	ret
.Lfe3:
	.size	 release,.Lfe3-release
	.ident	"GCC: (GNU) 2.96 20000731 (Red Hat Linux 7.1 2.96-98)"
