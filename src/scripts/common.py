"""Utilitarios compartilhados pelos scripts de automacao de src/scripts.

Substituem os antigos scripts .ps1 (Windows/PowerShell) por comandos Python
puros, que funcionam do mesmo jeito em Windows, Linux, macOS e WSL. Todos os
caminhos sao relativos ao diretorio atual, entao os comandos deste pacote
devem ser executados a partir da raiz do repositorio (mesma convencao que
'python main.py <arquivo>' ja segue).
"""

import ctypes
import os
import shutil
import subprocess
import sys
from pathlib import Path

OUTPUT_DIR = Path("output")
OUTPUT_CLASSES_DIR = OUTPUT_DIR / "classes"
TOOLS_DIR = Path("tools")
GRAMMAR_DIR = Path("grammar")
GENERATED_DIR = Path("generated")
TESTS_DIR = Path("tests")

ANTLR_JAR = TOOLS_DIR / "antlr-4.13.2-complete.jar"
JASMIN_JAR = TOOLS_DIR / "jasmin.jar"


class ScriptError(RuntimeError):
    """Falha esperada de um script de automacao (mensagem limpa, sem traceback)."""


def _use_color() -> bool:
    return not os.environ.get("NO_COLOR") and sys.stdout.isatty()


if sys.platform == "win32" and _use_color():
    try:
        kernel32 = ctypes.windll.kernel32
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
    except Exception:
        pass

_COLORS = {"green": "\033[32m", "red": "\033[31m", "yellow": "\033[33m", "reset": "\033[0m"}


def _colorize(text: str, color: str) -> str:
    if not _use_color():
        return text
    return f"{_COLORS[color]}{text}{_COLORS['reset']}"


def print_header(text: str) -> None:
    print("=" * 40)
    print(text)
    print("=" * 40)


def print_pass(text: str = "PASSOU") -> None:
    print(_colorize(text, "green"))


def print_fail(text: str = "FALHOU") -> None:
    print(_colorize(text, "red"))


def log_implicit(message: str) -> None:
    """Avisa, na saida de erro padrao, que uma etapa foi executada automaticamente."""
    print(_colorize(f"[implicito] {message}", "yellow"), file=sys.stderr)


def require_repo_root() -> None:
    if not JASMIN_JAR.exists():
        raise ScriptError(
            "tools/jasmin.jar nao encontrado. Execute este comando a partir da raiz do repositorio."
        )


def find_java() -> str:
    """Localiza o executavel do java em qualquer SO.

    Tenta 'java' (Linux/macOS/Windows nativo) e 'java.exe' (necessario ao
    rodar Python dentro do WSL, onde o PATH herdado do Windows so resolve a
    extensao explicita), depois cai para JAVA_HOME/bin caso nenhum dos dois
    esteja no PATH.
    """
    for candidate_name in ("java", "java.exe"):
        found = shutil.which(candidate_name)
        if found:
            return found

    java_home = os.environ.get("JAVA_HOME")
    if java_home:
        for exe_name in ("java", "java.exe"):
            candidate = Path(java_home) / "bin" / exe_name
            if candidate.exists():
                return str(candidate)

    raise ScriptError(
        "java nao encontrado no PATH nem em JAVA_HOME. Instale o JDK e garanta "
        "que o comando 'java' esteja acessivel no terminal."
    )


def _java_opts() -> list[str]:
    """Opcoes extras de JVM via variavel de ambiente JSS_JAVA_OPTS (ex.: '-Xmx64m')."""
    raw = os.environ.get("JSS_JAVA_OPTS", "")
    return raw.split() if raw else []


def run_java_jar(jar_path: Path, args: list[str], **kwargs) -> subprocess.CompletedProcess:
    java = find_java()
    cmd = [java, *_java_opts(), "-jar", str(jar_path), *args]
    return subprocess.run(cmd, **kwargs)


def run_java_class(
    classpath_dir: Path,
    class_name: str,
    *,
    stdin_text: str | None = None,
    capture: bool = False,
) -> subprocess.CompletedProcess:
    java = find_java()
    cmd = [java, *_java_opts(), "-cp", str(classpath_dir), class_name]
    if capture:
        return subprocess.run(cmd, input=stdin_text, capture_output=True, text=True)
    return subprocess.run(cmd, input=stdin_text, text=True if stdin_text is not None else None)
