class Ponto {
    int x;
    int y;

    Ponto constructor(int x, int y) {
        this.x = x;
        this.y = y;
    }

    int soma() {
        return this.x + this.y;
    }
}

function void main() {
    let Ponto p = new Ponto(1, 2);
    let int resultado = p.soma();

    console.log("Resultado:", resultado);
}