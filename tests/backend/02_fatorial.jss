function int fatorial(int n) {
    if (n > 1) {
        return n * fatorial(n - 1);
    } else {
        return 1;
    }
}

function void main() {
    let int numero = 5;
    let int resultado = fatorial(numero);
    console.log("Fatorial:", resultado);
}
