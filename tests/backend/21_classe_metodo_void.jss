class Contador {
    int valor;

    Contador constructor(int valor) {
        this.valor = valor;
    }

    void incrementar(int quantidade) {
        this.valor = this.valor + quantidade;
    }
}

function void main() {
    let Contador c = new Contador(10);

    c.incrementar(5);
    c.incrementar(15);

    console.log("Valor:", c.valor);
}
