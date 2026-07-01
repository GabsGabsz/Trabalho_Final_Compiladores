.class public MatrizHelper
.super java/lang/Object

.field public matriz [[I

.method public <init>()V
    .limit stack 300
    .limit locals 300
    aload_0
    invokespecial java/lang/Object/<init>()V
    aload_0
    iconst_3
    anewarray [I
    dup
    iconst_0
    iconst_3
    newarray int
    aastore
    dup
    iconst_1
    iconst_3
    newarray int
    aastore
    dup
    iconst_2
    iconst_3
    newarray int
    aastore
    putfield MatrizHelper/matriz [[I
    iconst_0
    istore 1
for_start_0:
    iload 1
    iconst_3
    if_icmplt cmp_true_2
    iconst_0
    goto cmp_end_3
cmp_true_2:
    iconst_1
cmp_end_3:
    ifeq for_end_1
    iconst_0
    istore 2
for_start_4:
    iload 2
    iconst_3
    if_icmplt cmp_true_6
    iconst_0
    goto cmp_end_7
cmp_true_6:
    iconst_1
cmp_end_7:
    ifeq for_end_5
    aload_0
    getfield MatrizHelper/matriz [[I
    iload 1
    aaload
    iload 2
    iconst_0
    iastore
    iload 2
    iconst_1
    iadd
    istore 2
    goto for_start_4
for_end_5:
    iload 1
    iconst_1
    iadd
    istore 1
    goto for_start_0
for_end_1:
    return
.end method

.method public setValor(III)V
    .limit stack 300
    .limit locals 300
    aload_0
    getfield MatrizHelper/matriz [[I
    iload 1
    aaload
    iload 2
    iload 3
    iastore
    return
.end method

.method public getValor(II)I
    .limit stack 300
    .limit locals 300
    aload_0
    getfield MatrizHelper/matriz [[I
    iload 1
    aaload
    iload 2
    iaload
    ireturn
    iconst_0
    ireturn
.end method

.method public imprimir()V
    .limit stack 300
    .limit locals 300
    iconst_0
    istore 1
for_start_8:
    iload 1
    iconst_3
    if_icmplt cmp_true_10
    iconst_0
    goto cmp_end_11
cmp_true_10:
    iconst_1
cmp_end_11:
    ifeq for_end_9
    iconst_0
    istore 2
for_start_12:
    iload 2
    iconst_3
    if_icmplt cmp_true_14
    iconst_0
    goto cmp_end_15
cmp_true_14:
    iconst_1
cmp_end_15:
    ifeq for_end_13
    getstatic java/lang/System/out Ljava/io/PrintStream;
    aload_0
    getfield MatrizHelper/matriz [[I
    iload 1
    aaload
    iload 2
    iaload
    invokevirtual java/io/PrintStream/print(I)V
    getstatic java/lang/System/out Ljava/io/PrintStream;
    invokevirtual java/io/PrintStream/println()V
    iload 2
    iconst_1
    iadd
    istore 2
    goto for_start_12
for_end_13:
    iload 1
    iconst_1
    iadd
    istore 1
    goto for_start_8
for_end_9:
    return
.end method

