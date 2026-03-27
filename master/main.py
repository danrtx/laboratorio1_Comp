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

    # Permitir pasar archivo por argumento
    file = "script.dsl"
    if len(sys.argv) > 1:
        file = sys.argv[1]

    # Validar que el archivo existe
    if not os.path.exists(file):
        print(f"[ERROR] No existe el archivo: {file}")
        return

    # Cargar archivo DSL
    input_stream = FileStream(file)

    # Lexer y parser
    lexer = DevOpsDSLLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = DevOpsDSLParser(tokens)

    # 🔥 Manejo de errores sintácticos
    parser.removeErrorListeners()
    parser.addErrorListener(ConsoleErrorListener())

    tree = parser.program()

    print("[INFO] Árbol sintáctico generado\n")

    # Inicializar sistema
    executor = Executor()
    interpreter = Interpreter(executor)

    # Ejecutar
    interpreter.visit(tree)


if __name__ == "__main__":
    main()