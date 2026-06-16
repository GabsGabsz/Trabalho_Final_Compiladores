class Caixa {
    int valor;

    Caixa constructor(int valor) {
        this.valor = valor;
    }

    void somar(int x) {
        this.valor += x;
    }
}

function void main() {
    let Caixa c = new Caixa(10);
    let int[2] numeros = [5, 8];

    c.somar(15);
    numeros[0] += 20;
    numeros[1] *= 2;

    console.log("Caixa:", c.valor);
    console.log("Vetor:", numeros[0] + numeros[1]);
}
