let int soma = 0;
let int j;

for (j = 0; j < 3; j = j + 1) {
    soma = soma + j;
}

let int a;
let int b;
for (a = 0, b = 10; a < b; a = a + 1, b = b - 1) {
    soma = soma + 1;
}

for (;;) {
    break;
}

for (let int i = 0, limite = 4; i < limite; i = i + 1) {
    soma = soma + i;
}

console.log(soma);
