function void main() {
    let int[3] numeros = [1, 2, 3];

    numeros[0] = 10;
    numeros[1] = numeros[0] + 5;

    console.log("Valor:", numeros[1]);
}