class Calculadora {
    int base;

    Calculadora constructor(int base) {
        this.base = base;
    }

    int soma(int a, int b) {
        return this.base + a + b;
    }
}

function void main() {
    let Calculadora calc = new Calculadora(10);
    let int resultado = calc.soma(2, 3);

    console.log("Resultado:", resultado);
}
