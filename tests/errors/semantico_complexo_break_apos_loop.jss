function int buscarIndice(int[5] valores, int alvo) {
    for (let int i = 0; i < 5; i = i + 1) {
        if (valores[i] == alvo) {
            return i;
        }
    }
    if (alvo < 0) {
        break;
    }
    return -1;
}

function void main() {
    let int[5] numeros = [10, 20, 30, 40, 50];
    let int pos = buscarIndice(numeros, 30);
    console.log("Posicao:", pos);
}
