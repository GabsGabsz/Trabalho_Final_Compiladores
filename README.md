
## Execucao oficial solicitada pelo professor

O ponto de entrada principal fica na raiz do projeto. Assim, a execucao pode ser feita diretamente com:

```powershell
python main.py arquivo.jss
```

Para gerar codigo Jasmin:

```powershell
python main.py --jasmin arquivo.jss
```

O arquivo `src/main.py` contem a implementacao real da linha de comando; o `main.py` da raiz apenas chama esse modulo para atender ao formato de execucao pedido.

# Compilador JSS - Java Script Simplificado

Projeto final da disciplina de Compiladores 2026.1. O projeto implementa um compilador para a linguagem Java Script Simplificado (JSS), com front-end e back-end usando ANTLR4, Python e Jasmin/JVM.

## 1. Requisitos

- Java JDK instalado e disponível no terminal pelo comando `java`.
- Python 3 instalado e disponível no terminal pelo comando `python`.
- PowerShell para executar os scripts `.ps1`.
- ANTLR 4.13.2, já incluído em `tools/antlr-4.13.2-complete.jar`.
- Jasmin, já incluído em `tools/jasmin.jar`.

Instale a dependência Python com:

```powershell
python -m pip install -r requirements.txt
```

O arquivo `requirements.txt` contém:

```text
antlr4-python3-runtime==4.13.2
```

## 2. Estrutura do projeto

```text
grammar/       Gramáticas ANTLR do lexer e parser
generated/     Arquivos Python gerados pelo ANTLR
src/           Código-fonte do compilador
scripts/       Scripts auxiliares de geração, testes e execução
tests/         Programas JSS de sucesso, erro e back-end
tools/         JARs do ANTLR e do Jasmin
output/        Arquivos Jasmin e classes geradas durante a execução
```

## 3. Gerar o parser

Caso seja necessário regenerar os arquivos em `generated/`, execute:

```powershell
.\scripts\generate_parser.ps1
```

## 4. Executar o front-end

O compilador lê o programa JSS pela entrada padrão. Exemplo com um arquivo válido:

```powershell
Get-Content -Raw tests\success\01_variaveis.jss | python main.py
```

Saída esperada:

```text
OK: programa valido.
```

Exemplo com erro semântico:

```powershell
Get-Content -Raw tests\errors\semantico_variavel_nao_declarada.jss | python main.py
```

Saída esperada:

```text
ERRO SEMANTICO na linha ..., coluna ...: identificador 'x' nao declarado.
```

## 5. Executar o back-end Jasmin

Para gerar o código Jasmin:

```powershell
Get-Content -Raw tests\backend\29_programa_completo.jss | python main.py --jasmin
```

Saída esperada:

```text
OK: codigo Jasmin gerado em output\Main.j.
```

Para montar os arquivos `.j` em bytecode JVM:

```powershell
.\scripts\assemble_jasmin.ps1
```

Para executar a classe principal:

```powershell
.\scripts\run_jasmin_class.ps1
```

## 6. Executar os testes

Testes do front-end:

```powershell
.\scripts\run_tests.ps1
```

Testes do back-end:

```powershell
.\scripts\run_backend_tests.ps1
```

Todos os testes:

```powershell
.\scripts\run_all_tests.ps1
```

Também é possível verificar os arquivos Python com:

```powershell
python -m compileall src generated
```

## 7. Recursos implementados

### Front-end

- Análise léxica com ANTLR.
- Análise sintática com ANTLR.
- Análise semântica com escopos, tipos e validações.
- Mensagens de erro léxico, sintático e semântico com linha e coluna.
- Leitura pela entrada padrão e saída pela saída padrão.
- Identificadores case-sensitive.
- Variáveis e constantes com escopo global e local.
- Funções, parâmetros, chamadas e recursão.
- Verificação de `main` sem parâmetros quando declarada.
- Vetores com tamanho fixo e inicialização por lista.
- Classes, atributos, constructor, métodos, objetos e `this`.
- Verificação de constantes, inclusive objetos constantes.
- Verificação de `break` apenas dentro de laços.
- Verificação de tipos em `if`, `while`, `for`, `return`, `input`, operadores e casts.

### Back-end

O back-end traduz a parse tree para Jasmin/JVM e gera bytecode executável.

Recursos suportados no back-end:

- Tipos `int`, `real`, `str` e `bool`.
- Variáveis locais e globais.
- Funções globais, chamadas e recursão.
- `main` Java gerada automaticamente.
- `if`, `else if`, `else`, `while`, `for` e `break`.
- `return` para funções `void`, `int`, `real`, `str`, `bool` e objetos.
- `console.log` com múltiplos argumentos separados por espaço.
- `input` com uma ou mais variáveis.
- Casts entre tipos primitivos permitidos pela especificação.
- Vetores locais e globais.
- Leitura e escrita em posições de vetor.
- Classes geradas em arquivos `.j` separados.
- Objetos com `new`, constructor, atributos e métodos.
- Acesso `this.campo` e `objeto.campo`.
- Chamada `objeto.metodo(...)`.
- Operadores aritméticos, relacionais, lógicos, potência, atribuições compostas, incremento e decremento.
- Aritmética mista `int`/`real` com conversão implícita para `real`.
- Concatenação de strings com `+`.
- Curto-circuito em `&&` e `||`.

## 8. Exemplo de programa JSS

```jss
class Produto {
    str nome;
    real preco;
    int quantidade;

    Produto constructor(str nome, real preco, int quantidade) {
        this.nome = nome;
        this.preco = preco;
        this.quantidade = quantidade;
    }

    void aumentar(int qtd) {
        this.quantidade += qtd;
    }

    real total() {
        return this.preco * real(this.quantidade);
    }
}

function int dobro(int x) {
    return x * 2;
}

function void main() {
    let Produto p = new Produto("Banana", 3.5, 4);
    let int[3] numeros = [1, 2, 3];

    numeros[0] += dobro(5);
    p.aumentar(numeros[1]);

    let real total = p.total() + real(numeros[0] ** 2);

    console.log("Produto:", p.nome);
    console.log("Quantidade:", p.quantidade);
    console.log("Numero:", numeros[0]);
    console.log("Total:", total);
}
```

Saída esperada:

```text
Produto: Banana
Quantidade: 6
Numero: 11
Total: 142.0
```

## 9. Observação sobre a entrega

Para submissão, não é necessário incluir a pasta `.venv`, arquivos `__pycache__`, arquivos `.pyc` ou arquivos gerados dentro de `output/classes`.

## Entrada por arquivo

Além da entrada padrão, o compilador também aceita o caminho de um arquivo `.jss` como argumento de linha de comando:

```powershell
python main.py tests\prof\1_basics.jss
python main.py --jasmin tests\prof\1_basics.jss
```

Esse modo facilita a execução conforme a especificação do trabalho e os testes fornecidos pelo professor.
