let int soma = 0;
let int j;

for (let int i = 0; i < 3; i = i + 1) {
    soma = soma + i;
}

for (j = 0; j < 3; j = j + 1) {
    soma = soma + j;
}

let int a;
let int b;
let int voltas = 0;
for (a = 0, b = 10; a < b; a = a + 1, b = b - 1) {
    voltas = voltas + 1;
}

let int parada = 0;
for (;;) {
    parada = parada + 1;
    if (parada >= 4) {
        break;
    }
}

console.log("Soma:", soma);
console.log("Voltas:", voltas);
console.log("Parada:", parada);
