class Ponto {
    int x;
    int y;

    Ponto constructor(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

function void main() {
    let Ponto p = new Ponto(1, 2);

    p.x = 50;
    p.y = 70;

    console.log("Soma:", p.x + p.y);
}
