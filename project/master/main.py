import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from antlr4 import *
from antlr4.error.ErrorListener import ConsoleErrorListener
from parser.DevOpsDSLLexer import DevOpsDSLLexer
from parser.DevOpsDSLParser import DevOpsDSLParser
from interpreter.interpreter import Interpreter
from executor.executor import Executor


def main():
    print("[INFO] Iniciando sistema DSL...\n")

    file = "script.dsl"
    if len(sys.argv) > 1:
        file = sys.argv[1]

    if not os.path.exists(file):
        print(f"[ERROR] No existe el archivo: {file}")
        return

    input_stream = FileStream(file)
    lexer = DevOpsDSLLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    tokens.fill()

    print("=" * 60)
    print("TOKENS GENERADOS POR EL LEXER")
    print("=" * 60)
    for token in tokens.tokens:
        nombre = lexer.ruleNames[token.type - 1] if 0 < token.type <= len(lexer.ruleNames) else ("EOF" if token.type == -1 else "SYMBOL")
        print(f"  [{nombre}] -> \'{token.text}\'")
    print()

    parser = DevOpsDSLParser(tokens)
    parser.removeErrorListeners()
    parser.addErrorListener(ConsoleErrorListener())
    tree = parser.program()

    print("=" * 60)
    print("ARBOL SINTACTICO")
    print("=" * 60)
    print(tree.toStringTree(recog=parser))
    print()

    print("[INFO] Arbol sintactico generado\n")

    executor = Executor()
    interpreter = Interpreter(executor)

    print("=" * 60)
    print("INTERPRETACION Y EJECUCION")
    print("=" * 60)
    print()

    interpreter.visit(tree)


if __name__ == "__main__":
    main()
