class ContaBancaria {
    real saldo;
    str titular;

    ContaBancaria constructor(str titular, real saldo) {
        this.titular = titular;
        this.saldo = saldo;
    }

    void depositar(real valor) {
        this.saldo += valor;
    }
}

function real calcularJuros(real saldo, real taxa) {
    return saldo * taxa;
}

function void main() {
    const ContaBancaria conta = new ContaBancaria("Carlos", 1000.0);
    let real juros = calcularJuros(conta.saldo, 0.05);
    conta.depositar(juros);
    console.log("Saldo:", conta.saldo);

    conta = new ContaBancaria("Outro", 0.0);
}
