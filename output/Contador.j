.class public Contador
.super java/lang/Object

.field public valor I

.method public <init>()V
    .limit stack 300
    .limit locals 300
    aload_0
    invokespecial java/lang/Object/<init>()V
    aload_0
    iconst_0
    putfield Contador/valor I
    return
.end method

.method public incrementar()V
    .limit stack 300
    .limit locals 300
    aload_0
    aload_0
    getfield Contador/valor I
    iconst_1
    iadd
    putfield Contador/valor I
    return
.end method

.method public decrementar()V
    .limit stack 300
    .limit locals 300
    aload_0
    aload_0
    getfield Contador/valor I
    iconst_1
    isub
    putfield Contador/valor I
    return
.end method

.method public getValor()I
    .limit stack 300
    .limit locals 300
    aload_0
    getfield Contador/valor I
    ireturn
    iconst_0
    ireturn
.end method

