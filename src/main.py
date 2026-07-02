import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
SRC_DIR = ROOT_DIR / "src"
GENERATED_DIR = ROOT_DIR / "generated"

if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

if str(GENERATED_DIR) not in sys.path:
    sys.path.insert(0, str(GENERATED_DIR))

from errors.compiler_error import CompilerError
from frontend.lexical import LexicalAnalyzer
from frontend.syntactic import SyntacticAnalyzer
from semantic.analyzer import SemanticAnalyzer
from backend.jasmin_generator import JasminGenerator
from scripts import assemble_jasmin, common as scripts_common, run_jasmin_class

def read_source_code(args: list[str]) -> str:
    """Le o codigo-fonte JSS: por caminho de arquivo (args[0]) ou pela entrada padrao."""
    file_args = [arg for arg in args if not arg.startswith("--")]

    if file_args:
        input_path = Path(file_args[0])

        if not input_path.exists():
            raise FileNotFoundError(f"arquivo nao encontrado: {input_path}")

        if not input_path.is_file():
            raise FileNotFoundError(f"caminho informado nao e um arquivo: {input_path}")

        return input_path.read_text(encoding="utf-8-sig")

    # Le os bytes crus e decodifica como utf-8-sig: no Windows, sys.stdin.read()
    # usa a codepage legada do console (ex.: cp1252) por padrao, o que corrompe
    # um BOM UTF-8 em vez de remove-lo do inicio do texto.
    return sys.stdin.buffer.read().decode("utf-8-sig")

def main() -> int:
    args = sys.argv[1:]
    # --assemble implica --jasmin (precisa do .j para montar); --run implica --assemble.
    do_run = "--run" in args
    do_assemble = do_run or "--assemble" in args
    generate_jasmin = do_assemble or "--jasmin" in args

    try:
        source_code = read_source_code(args)

        if not source_code.strip():
            print("ERRO SINTATICO na linha 1, coluna 1: entrada vazia.")
            return 1

        lexical_analyzer = LexicalAnalyzer()
        token_stream = lexical_analyzer.analyze(source_code)

        syntactic_analyzer = SyntacticAnalyzer()
        tree, _ = syntactic_analyzer.analyze(token_stream)

        semantic_analyzer = SemanticAnalyzer()
        semantic_analyzer.analyze(tree)

        if not generate_jasmin:
            print("OK: programa valido.")
            return 0

        generator = JasminGenerator()
        output_path = generator.generate(tree, "output/Main.j")
        print(f"OK: codigo Jasmin gerado em {output_path}.")
        sys.stdout.flush()

        if do_assemble:
            scripts_common.log_implicit(
                "--assemble/--run pedido: montando output/*.j em output/classes/*.class "
                "via tools/jasmin.jar (equivalente a 'python -m src.scripts.assemble_jasmin')."
            )
            assemble_jasmin.assemble()

        if do_run:
            scripts_common.log_implicit(
                "--run pedido: executando 'java -cp output/classes Main' "
                "(equivalente a 'python -m src.scripts.run_jasmin_class')."
            )
            result = run_jasmin_class.run_class()
            return result.returncode

        return 0

    except CompilerError as error:
        print(error)
        return 1

    except FileNotFoundError as error:
        print(f"ERRO: {error}")
        return 1

    except NotImplementedError as error:
        print(f"ERRO BACKEND: {error}")
        return 1

    except scripts_common.ScriptError as error:
        print(f"ERRO: {error}")
        return 1

    except Exception as error:
        print(f"ERRO INTERNO: {error}")
        return 1

if __name__ == "__main__":
    raise SystemExit(main())