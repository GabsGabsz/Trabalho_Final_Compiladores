
# Compilador JSS - Java Script Simplificado

Compilador para o JSS (Java Script Simplificado), uma linguagem de ensino com sintaxe inspirada em
JavaScript e tipagem forte, desenvolvido como projeto final da disciplina de Compiladores (UFPI, 2026.1).
O projeto implementa um front-end completo (análise léxica, sintática e semântica) e um back-end que gera
bytecode executável para a JVM via Jasmin, usando ANTLR4 e Python.

O ponto de entrada fica na raiz do repositório:

```bash
python main.py arquivo.jss
```

Para gerar código Jasmin (back-end):

```bash
python main.py --jasmin arquivo.jss
```

A implementação da linha de comando fica em `src/main.py`; o `main.py` na raiz apenas a encaminha, para
manter o comando de execução simples a partir da raiz do repositório.

## 1. Requisitos

- Java JDK instalado e disponível no terminal pelo comando `java`.
- Python 3 instalado e disponível no terminal pelo comando `python`.
- ANTLR 4.13.2, já incluído em `tools/antlr-4.13.2-complete.jar`.
- Jasmin, já incluído em `tools/jasmin.jar`.

Nenhum shell específico é necessário: todos os scripts auxiliares (`src/scripts/`) são Python puro e
funcionam da mesma forma em Windows, Linux, macOS ou WSL.

Instale a dependência Python com:

```bash
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
src/scripts/   Scripts auxiliares de geração, testes e execução (Python, multiplataforma)
tests/         Programas JSS de sucesso, erro e back-end
tools/         JARs do ANTLR e do Jasmin
output/        Arquivos Jasmin e classes geradas durante a execução
```

## 3. Gerar o parser

Caso seja necessário regenerar os arquivos em `generated/`, execute:

```bash
python -m src.scripts.generate_parser
```

## 4. Executar o front-end

O compilador recebe o caminho do arquivo `.jss` como argumento. Exemplo com um arquivo válido:

```bash
python main.py tests/success/01_variaveis.jss
```

Saída esperada:

```text
OK: programa valido.
```

Exemplo com erro semântico:

```bash
python main.py tests/errors/semantico_variavel_nao_declarada.jss
```

Saída esperada:

```text
ERRO SEMANTICO na linha ..., coluna ...: identificador 'x' nao declarado.
```

## 5. Executar o back-end Jasmin

Para gerar o código Jasmin:

```bash
python main.py --jasmin tests/backend/29_programa_completo.jss
```

Saída esperada:

```text
OK: codigo Jasmin gerado em output\Main.j.
```

Para montar os arquivos `.j` em bytecode JVM:

```bash
python -m src.scripts.assemble_jasmin
```

Para executar a classe principal:

```bash
python -m src.scripts.run_jasmin_class
```

### 5.1. Atalho: gerar, montar e executar em um só comando

`main.py` aceita as flags `--assemble` (gera o Jasmin e já monta o bytecode) e `--run` (gera, monta e
executa a classe `Main`), como alternativa aos três passos manuais acima. Sempre que uma dessas flags
dispara uma etapa extra automaticamente, uma linha `[implicito] ...` é impressa na saída de erro (stderr)
explicando o que foi feito. A saída padrão (stdout) continua imprimindo exatamente a mesma linha
`OK: codigo Jasmin gerado em ...` de sempre, seguida da saída real do programa:

```bash
python main.py --run tests/backend/29_programa_completo.jss
```

### 5.2. Comandos Java diretos (sem os scripts Python)

Os scripts em `src/scripts/` só automatizam passos repetitivos (criar pastas, montar múltiplos arquivos
`.j` de uma vez, etc.). Eles não fazem nada que não possa ser feito digitando os comandos `java` abaixo
diretamente.

Regenerar o parser (equivalente a `python -m src.scripts.generate_parser`):

```bash
java -jar tools/antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor -listener -Xexact-output-dir -o generated grammar/JSSLexer.g4 grammar/JSSParser.g4
```

Montar os arquivos `.j` gerados em bytecode JVM (equivalente a `python -m src.scripts.assemble_jasmin`):

```bash
mkdir -p output/classes
java -jar tools/jasmin.jar -d output/classes output/*.j
```

Executar a classe principal já montada (equivalente a `python -m src.scripts.run_jasmin_class`):

```bash
java -cp output/classes Main
```

## 6. Executar os testes

Todos os comandos abaixo funcionam sem alteração em Windows, Linux, macOS ou WSL.

Testes do front-end:

```bash
python -m src.scripts.run_tests
```

Testes do back-end:

```bash
python -m src.scripts.run_backend_tests
```

Testes com os arquivos fornecidos pelo professor (`tests/prof`):

```bash
python -m src.scripts.run_professor_tests
```

Todos os testes (front-end e depois back-end, parando no primeiro conjunto que falhar):

```bash
python -m src.scripts.run_all_tests
```

### 6.1. Executar cada teste do professor individualmente pelo back-end

Também é possível rodar o pipeline completo do back-end (gerar Jasmin, montar e executar) para cada arquivo
de `tests/prof` separadamente, usando o atalho `--run` (seção 5.1) em vez do script agregador. Os arquivos
`1` a `5` são programas válidos e produzem um `.class` executável; os arquivos `6`, `7` e `8` são casos
negativos fornecidos pelo professor (devem falhar já na geração do Jasmin, com `ERRO SEMANTICO`).

```bash
python main.py --run tests/prof/1_basics.jss
python main.py --run tests/prof/2_operators.jss
python main.py --run tests/prof/3_control_flow.jss
python main.py --run tests/prof/5_classes.jss
```

```bash
# 4_strings_casts.jss pede entrada: três números e depois dois nomes
printf "1 2 3\nAna Bia\n" | python main.py --run tests/prof/4_strings_casts.jss
```

```bash
# 6_functions.jss, 7_errors.jss e 8_erros_funcao.jss são casos negativos: cada um já
# falha no próprio "--jasmin" (não chegam a montar/rodar), com ERRO SEMANTICO ou SINTATICO
python main.py --jasmin tests/prof/6_functions.jss
python main.py --jasmin tests/prof/7_errors.jss
python main.py --jasmin tests/prof/8_erros_funcao.jss
```

Também é possível verificar os arquivos Python com:

```bash
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
- Funções, parâmetros (inclusive de tipos derivados, como vetores e objetos), chamadas e recursão.
- Verificação de `main` sem parâmetros quando declarada.
- Vetores com tamanho fixo e inicialização por lista, inclusive multidimensionais (`int[3][3]`).
- Classes, atributos, constructor, métodos, objetos e `this`.
- Verificação de constantes, inclusive objetos constantes.
- Verificação de `break` apenas dentro de laços.
- Verificação de tipos em `if`, `while`, `for`, `return`, `input`, operadores e casts.
- `for` com declaração ou atribuições no cabeçalho (inclusive múltiplas atribuições separadas por vírgula), com inicialização, condição e atualização opcionais.
- Verificação de que função ou método não pode retornar vetor (retorno de objeto é permitido).
- Comandos soltos fora de qualquer função, no nível superior do arquivo.

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
- Comparação `==`/`!=` entre objetos, strings e `null` (comparação de referência da JVM).
- Comandos soltos fora de função executados sempre antes de qualquer método, inclusive `main`.

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

## 9. Arquivos gerados e de ambiente

A pasta `.venv/`, os diretórios `__pycache__/`, arquivos `.pyc` e o conteúdo gerado em `output/classes/`
não fazem parte do código-fonte: são artefatos do ambiente virtual Python e do build, recriados a
qualquer momento a partir dos comandos das seções acima.

## Entrada pela entrada padrão (stdin)

Além do caminho de arquivo como argumento, o compilador também aceita o programa pela entrada padrão
(stdin), conforme a especificação da linguagem. Isso também é útil para compor com outras ferramentas ou
pipelines. A sintaxe de redirecionamento é a única parte que muda por shell:

```bash
# Bash/zsh (Linux, macOS, WSL)
python main.py < tests/prof/1_basics.jss
python main.py --jasmin < tests/prof/1_basics.jss
```

```powershell
# PowerShell (Windows)
Get-Content -Raw tests\prof\1_basics.jss | python main.py
Get-Content -Raw tests\prof\1_basics.jss | python main.py --jasmin
```

Os dois modos (arquivo ou stdin) são equivalentes; o modo por arquivo é o mais prático no dia a dia.
