function void main() {
    let int i = 0;
    let int soma = 0;

    while (i < 5) {
        soma = soma + i;
        i = i + 1;
    }

    for (let int j = 0; j < 10; j = j + 1) {
        if (j == 3) {
            break;
        } else {
            soma = soma + j;
        }
    }

    console.log("Soma:", soma);
}