.class public Pessoa
.super java/lang/Object

.field public nome Ljava/lang/String;
.field public idade I

.method public <init>(Ljava/lang/String;I)V
    .limit stack 300
    .limit locals 300
    aload_0
    invokespecial java/lang/Object/<init>()V
    aload_0
    aload 1
    putfield Pessoa/nome Ljava/lang/String;
    aload_0
    iload 2
    putfield Pessoa/idade I
    return
.end method

.method public getNome()Ljava/lang/String;
    .limit stack 300
    .limit locals 300
    aload_0
    getfield Pessoa/nome Ljava/lang/String;
    areturn
    ldc ""
    areturn
.end method

.method public getIdade()I
    .limit stack 300
    .limit locals 300
    aload_0
    getfield Pessoa/idade I
    ireturn
    iconst_0
    ireturn
.end method

.method public apresentar()V
    .limit stack 300
    .limit locals 300
    getstatic java/lang/System/out Ljava/io/PrintStream;
    ldc "Nome:"
    invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
    getstatic java/lang/System/out Ljava/io/PrintStream;
    ldc " "
    invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
    getstatic java/lang/System/out Ljava/io/PrintStream;
    aload_0
    getfield Pessoa/nome Ljava/lang/String;
    invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
    getstatic java/lang/System/out Ljava/io/PrintStream;
    ldc " "
    invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
    getstatic java/lang/System/out Ljava/io/PrintStream;
    ldc "Idade:"
    invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
    getstatic java/lang/System/out Ljava/io/PrintStream;
    ldc " "
    invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
    getstatic java/lang/System/out Ljava/io/PrintStream;
    aload_0
    getfield Pessoa/idade I
    invokevirtual java/io/PrintStream/print(I)V
    getstatic java/lang/System/out Ljava/io/PrintStream;
    invokevirtual java/io/PrintStream/println()V
    return
.end method

.method public aniversario()V
    .limit stack 300
    .limit locals 300
    aload_0
    aload_0
    getfield Pessoa/idade I
    iconst_1
    iadd
    putfield Pessoa/idade I
    getstatic java/lang/System/out Ljava/io/PrintStream;
    aload_0
    getfield Pessoa/nome Ljava/lang/String;
    invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
    getstatic java/lang/System/out Ljava/io/PrintStream;
    ldc " "
    invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
    getstatic java/lang/System/out Ljava/io/PrintStream;
    ldc "agora tem"
    invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
    getstatic java/lang/System/out Ljava/io/PrintStream;
    ldc " "
    invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
    getstatic java/lang/System/out Ljava/io/PrintStream;
    aload_0
    getfield Pessoa/idade I
    invokevirtual java/io/PrintStream/print(I)V
    getstatic java/lang/System/out Ljava/io/PrintStream;
    ldc " "
    invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
    getstatic java/lang/System/out Ljava/io/PrintStream;
    ldc "anos"
    invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
    getstatic java/lang/System/out Ljava/io/PrintStream;
    invokevirtual java/io/PrintStream/println()V
    return
.end method

