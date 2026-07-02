"""Monta os arquivos .j gerados em output/ para bytecode JVM (.class).

Equivalente universal de scripts/assemble_jasmin.ps1:
    python -m src.scripts.assemble_jasmin
"""

from pathlib import Path

from . import common


def assemble(
    output_dir: Path = common.OUTPUT_DIR,
    classes_dir: Path = common.OUTPUT_CLASSES_DIR,
) -> list[Path]:
    common.require_repo_root()

    classes_dir.mkdir(parents=True, exist_ok=True)
    for old_class in classes_dir.glob("*.class"):
        old_class.unlink()

    jasmin_files = sorted(output_dir.glob("*.j"))
    if not jasmin_files:
        raise common.ScriptError(f"nenhum arquivo .j encontrado em {output_dir}.")

    result = common.run_java_jar(
        common.JASMIN_JAR,
        ["-d", str(classes_dir), *[str(f) for f in jasmin_files]],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise common.ScriptError(f"jasmin falhou ao montar os arquivos:\n{result.stdout}{result.stderr}")

    return jasmin_files


def main(argv: list[str] | None = None) -> int:
    try:
        files = assemble()
    except common.ScriptError as error:
        print(f"ERRO: {error}")
        return 1
    print(f"OK: {len(files)} arquivo(s) .j montado(s) em {common.OUTPUT_CLASSES_DIR}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
