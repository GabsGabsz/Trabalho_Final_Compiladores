function void main() {
    let int soma = 0;

    for (let int i = 0; i < 10; i = i + 1) {
        if (i == 4) {
            break;
        }

        soma = soma + i;
    }

    console.log("Soma:", soma);
}
