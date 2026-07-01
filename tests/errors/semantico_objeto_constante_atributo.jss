class Ponto {
    int x;
    int y;

    Ponto constructor(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

function void main() {
    const Ponto p = new Ponto(1, 2);
    p.x = 10;
}