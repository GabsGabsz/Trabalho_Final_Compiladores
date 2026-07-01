class Retangulo {
    real largura;
    real altura;

    Retangulo constructor(real largura, real altura) {
        this.largura = largura;
        this.altura = altura;
    }

    real area() {
        return this.largura * this.altura;
    }
}

function void relatar(str nome, real valor) {
    console.log(nome + ": " + str(valor));
}

function void main() {
    let Retangulo r1 = new Retangulo(3.0, 4.0);
    let Retangulo r2 = new Retangulo(5.0);
    relatar("Area 1", r1.area());
    relatar("Area 2", r2.area());
}
