function void main() {
    let bool ativo = true;
    let bool bloqueado = false;

    if (ativo && !bloqueado) {
        console.log("Liberado");
    } else {
        console.log("Bloqueado");
    }
}
