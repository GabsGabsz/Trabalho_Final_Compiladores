let int totalChamadas = 0;

function int fatorial(int n) {
    totalChamadas = totalChamadas + 1;
    if (n <= 1) {
        return 1;
    } else {
        return n * fatorial(n - 1);
    }
}

class Pessoa {
    str nome;
    int idade;

    Pessoa constructor(str nome, int idade) {
        this.nome = nome;
        this.idade = idade;
    }

    str apresentar() {
        return "Nome: " + this.nome + " Idade: " + str(this.idade);
    }

    void aniversario() {
        this.idade = this.idade + 1;
    }
}

function void main() {
    let int[4] numeros = [1, 2, 3, 4];
    const int[3] fixos = [10, 20, 30];

    let int soma = 0;
    for (let int i = 0; i < 4; i = i + 1) {
        soma += numeros[i];
    }

    let int j = 0;
    while (j < 3) {
        soma += fixos[j];
        if (soma > 1000) {
            break;
        }
        j++;
    }

    for (j = 0; j < 2; j = j + 1) {
        soma--;
    }

    let bool ativo = true;
    let bool inativo = false;
    if (ativo && !inativo) {
        console.log("Logica ok");
    } else if (ativo || inativo) {
        console.log("Nao deveria cair aqui");
    } else {
        console.log("Nunca");
    }

    let real mediaReal = real(soma) / real(numeros[0]);
    let int potencia = 2 ** 5;
    let bool ehZero = bool(0);
    let str texto = "Total: " + str(soma) + " Media: " + str(mediaReal);

    console.log(texto);
    console.log("Fatorial de 5:", fatorial(5));
    console.log("Chamadas recursivas:", totalChamadas);
    console.log("Potencia:", potencia);
    console.log("Zero como bool:", ehZero);

    let Pessoa p = new Pessoa("Ana", 30);
    console.log(p.apresentar());
    p.aniversario();
    console.log("Nova idade:", p.idade);

    let Pessoa vazio = null;
    if (vazio == null) {
        console.log("Objeto nulo detectado");
    }
}
