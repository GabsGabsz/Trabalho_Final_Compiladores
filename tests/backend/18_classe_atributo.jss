class Ponto {
    int x;
    int y;

    Ponto constructor(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

function void main() {
    let Ponto p = new Ponto(10, 20);

    console.log("X:", p.x);
    console.log("Y:", p.y);
}
