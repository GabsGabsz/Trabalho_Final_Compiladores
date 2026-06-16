class Dobro {
    int valor;

    Dobro constructor(int valor) {
        this.valor = valor;
    }

    int calcular() {
        return this.valor * 2;
    }
}

class Triplo {
    int valor;

    Triplo constructor(int valor) {
        this.valor = valor;
    }

    int calcular() {
        return this.valor * 3;
    }
}

function void main() {
    let Dobro d = new Dobro(4);
    let Triplo t = new Triplo(5);

    let int resultado = d.calcular() + t.calcular();

    console.log("Resultado:", resultado);
}
