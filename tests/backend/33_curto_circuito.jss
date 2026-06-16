let int marcador = 0;

function bool alterar() {
    marcador = 10;
    return true;
}

function void main() {
    let bool a = false && alterar();
    console.log("A:", marcador, a);

    let bool b = true || alterar();
    console.log("B:", marcador, b);
}
