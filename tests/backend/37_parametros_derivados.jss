class Caixa {
    int valor;

    Caixa constructor(int valor) {
        this.valor = valor;
    }
}

function int somarVetor(int[5] valores) {
    let int soma = 0;
    for (let int i = 0; i < 5; i = i + 1) {
        soma = soma + valores[i];
    }
    return soma;
}

function int dobroDaCaixa(Caixa c) {
    return c.valor * 2;
}

let int[5] nums = [10, 20, 30, 40, 50];
let Caixa caixa = new Caixa(7);
console.log("Soma:", somarVetor(nums));
console.log("Dobro:", dobroDaCaixa(caixa));
