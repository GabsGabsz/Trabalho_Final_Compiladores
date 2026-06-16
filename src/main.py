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


def main() -> int:
    generate_jasmin = "--jasmin" in sys.argv

    source_code = sys.stdin.read().lstrip("\ufeff")

    if not source_code.strip():
        print("ERRO SINTATICO na linha 1, coluna 1: entrada vazia.")
        return 1

    try:
        lexical_analyzer = LexicalAnalyzer()
        token_stream = lexical_analyzer.analyze(source_code)

        syntactic_analyzer = SyntacticAnalyzer()
        tree, _ = syntactic_analyzer.analyze(token_stream)

        semantic_analyzer = SemanticAnalyzer()
        semantic_analyzer.analyze(tree)

        if generate_jasmin:
            generator = JasminGenerator()
            output_path = generator.generate(tree, "output/Main.j")
            print(f"OK: codigo Jasmin gerado em {output_path}.")
        else:
            print("OK: programa valido.")

        return 0

    except CompilerError as error:
        print(error)
        return 1

    except NotImplementedError as error:
        print(f"ERRO BACKEND: {error}")
        return 1

    except Exception as error:
        print(f"ERRO INTERNO: {error}")
        return 1


if __name__ == "__main__":
    sys.exit(main())