class Aluno {
    str nome;
    real nota;

    Aluno constructor(str nome, real nota) {
        this.nome = nome;
        this.nota = nota;
    }

    real bonificar(real extra) {
        return this.nota + extra;
    }

    str getNome() {
        return this.nome;
    }
}

function void main() {
    let Aluno aluno = new Aluno("Ana", 8.0);

    console.log("Aluno:", aluno.getNome());
    console.log("Nota:", aluno.bonificar(1.5));
}
