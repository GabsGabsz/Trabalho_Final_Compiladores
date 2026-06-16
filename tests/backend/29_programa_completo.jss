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
