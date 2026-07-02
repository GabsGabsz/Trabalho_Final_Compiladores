"""Regenera o lexer/parser Python a partir das gramaticas ANTLR.

Equivalente universal de scripts/generate_parser.ps1:
    python -m src.scripts.generate_parser
"""

from . import common


def generate() -> None:
    common.require_repo_root()
    args = [
        "-Dlanguage=Python3",
        "-visitor",
        "-listener",
        "-Xexact-output-dir",
        "-o", str(common.GENERATED_DIR),
        str(common.GRAMMAR_DIR / "JSSLexer.g4"),
        str(common.GRAMMAR_DIR / "JSSParser.g4"),
    ]
    result = common.run_java_jar(common.ANTLR_JAR, args)
    if result.returncode != 0:
        raise common.ScriptError("geracao do parser ANTLR falhou.")


def main(argv: list[str] | None = None) -> int:
    try:
        generate()
    except common.ScriptError as error:
        print(f"ERRO: {error}")
        return 1
    print(f"OK: parser regenerado em {common.GENERATED_DIR}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
