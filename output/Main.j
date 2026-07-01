.class public Main
.super java/lang/Object

.field static __scanner Ljava/util/Scanner;

.method public <init>()V
    aload_0
    invokespecial java/lang/Object/<init>()V
    return
.end method

.method static <clinit>()V
    .limit stack 300
    .limit locals 300
    new java/util/Scanner
    dup
    getstatic java/lang/System/in Ljava/io/InputStream;
    invokespecial java/util/Scanner/<init>(Ljava/io/InputStream;)V
    getstatic java/util/Locale/US Ljava/util/Locale;
    invokevirtual java/util/Scanner/useLocale(Ljava/util/Locale;)Ljava/util/Scanner;
    putstatic Main/__scanner Ljava/util/Scanner;
    return
.end method

.method public static main([Ljava/lang/String;)V
    .limit stack 300
    .limit locals 300
    new Pessoa
    dup
    ldc "Joao"
    bipush 30
    invokespecial Pessoa/<init>(Ljava/lang/String;I)V
    astore 1
    aload 1
    invokevirtual Pessoa/apresentar()V
    aload 1
    invokevirtual Pessoa/getNome()Ljava/lang/String;
    astore 2
    getstatic java/lang/System/out Ljava/io/PrintStream;
    ldc "Nome obtido:"
    invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
    getstatic java/lang/System/out Ljava/io/PrintStream;
    ldc " "
    invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
    getstatic java/lang/System/out Ljava/io/PrintStream;
    aload 2
    invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
    getstatic java/lang/System/out Ljava/io/PrintStream;
    invokevirtual java/io/PrintStream/println()V
    aload 1
    invokevirtual Pessoa/aniversario()V
    new Contador
    dup
    invokespecial Contador/<init>()V
    astore 3
    getstatic java/lang/System/out Ljava/io/PrintStream;
    ldc "Contador inicial:"
    invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
    getstatic java/lang/System/out Ljava/io/PrintStream;
    ldc " "
    invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
    getstatic java/lang/System/out Ljava/io/PrintStream;
    aload 3
    invokevirtual Contador/getValor()I
    invokevirtual java/io/PrintStream/print(I)V
    getstatic java/lang/System/out Ljava/io/PrintStream;
    invokevirtual java/io/PrintStream/println()V
    aload 3
    invokevirtual Contador/incrementar()V
    aload 3
    invokevirtual Contador/incrementar()V
    getstatic java/lang/System/out Ljava/io/PrintStream;
    ldc "Apos 2 incrementos:"
    invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
    getstatic java/lang/System/out Ljava/io/PrintStream;
    ldc " "
    invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
    getstatic java/lang/System/out Ljava/io/PrintStream;
    aload 3
    invokevirtual Contador/getValor()I
    invokevirtual java/io/PrintStream/print(I)V
    getstatic java/lang/System/out Ljava/io/PrintStream;
    invokevirtual java/io/PrintStream/println()V
    aload 3
    invokevirtual Contador/decrementar()V
    getstatic java/lang/System/out Ljava/io/PrintStream;
    ldc "Apos 1 decremento:"
    invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
    getstatic java/lang/System/out Ljava/io/PrintStream;
    ldc " "
    invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
    getstatic java/lang/System/out Ljava/io/PrintStream;
    aload 3
    invokevirtual Contador/getValor()I
    invokevirtual java/io/PrintStream/print(I)V
    getstatic java/lang/System/out Ljava/io/PrintStream;
    invokevirtual java/io/PrintStream/println()V
    new MatrizHelper
    dup
    invokespecial MatrizHelper/<init>()V
    astore 4
    aload 4
    iconst_0
    iconst_0
    iconst_1
    invokevirtual MatrizHelper/setValor(III)V
    aload 4
    iconst_0
    iconst_1
    iconst_2
    invokevirtual MatrizHelper/setValor(III)V
    aload 4
    iconst_1
    iconst_0
    iconst_3
    invokevirtual MatrizHelper/setValor(III)V
    aload 4
    iconst_1
    iconst_1
    iconst_4
    invokevirtual MatrizHelper/setValor(III)V
    aload 4
    iconst_1
    iconst_1
    invokevirtual MatrizHelper/getValor(II)I
    istore 5
    getstatic java/lang/System/out Ljava/io/PrintStream;
    ldc "Valor[1][1]:"
    invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
    getstatic java/lang/System/out Ljava/io/PrintStream;
    ldc " "
    invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
    getstatic java/lang/System/out Ljava/io/PrintStream;
    iload 5
    invokevirtual java/io/PrintStream/print(I)V
    getstatic java/lang/System/out Ljava/io/PrintStream;
    invokevirtual java/io/PrintStream/println()V
    getstatic java/lang/System/out Ljava/io/PrintStream;
    ldc "Matriz:"
    invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
    getstatic java/lang/System/out Ljava/io/PrintStream;
    invokevirtual java/io/PrintStream/println()V
    aload 4
    invokevirtual MatrizHelper/imprimir()V
    return
.end method

