	.file	"lock.c"
	.version	"01.01"
gcc2_compiled.:
.text
	.align 4
.globl make_lock
	.type	 make_lock,@function
make_lock:
	pushl %ebp
	movl %esp,%ebp
	subl $4,%esp
	pushl $4
	call malloc
	addl $4,%esp
	movl %eax,%eax
	movl %eax,-4(%ebp)
	movl -4(%ebp),%eax
	movl $0,(%eax)
	movl -4(%ebp),%edx
	movl %edx,%eax
	jmp .L1
	.p2align 4,,7
.L1:
	leave
	ret
.Lfe1:
	.size	 make_lock,.Lfe1-make_lock
	.align 4
.globl acquire
	.type	 acquire,@function
acquire:
        pushl %ebp
        movl %esp,%ebp
        nop
        movl 8(%ebp), %eax
        .p2align 4,,7
.L2:
        btsl $0,0(%eax)
        jc .L2
        .p2align 4,,7
.L3:
        leave
        ret
.Lfe2:
	.size	 acquire,.Lfe2-acquire
	.align 4
.globl release
	.type	 release,@function
release:
	pushl %ebp
	movl %esp,%ebp
	movl 8(%ebp),%eax
	movl $0,(%eax)
.L6:
	leave
	ret
.Lfe3:
	.size	 release,.Lfe3-release
	.ident	"GCC: (GNU) egcs-2.91.66 19990314/Linux (egcs-1.1.2 release)"
