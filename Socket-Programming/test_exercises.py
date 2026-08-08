"""Small no-network checks for the algorithms used in the exercise servers."""
import ast
from pathlib import Path

ROOT = Path(__file__).parent

def function_from(question, name):
    filename = ROOT / question / "server.py"
    tree = ast.parse(filename.read_text())
    function = next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == name)
    module = ast.Module(body=[function], type_ignores=[])
    namespace = {}
    exec(compile(module, str(filename), "exec"), namespace)
    return namespace[name]

calculate = function_from("q02", "calculate")
is_prime = function_from("q03", "is_prime")
is_palindrome = function_from("q07", "is_palindrome")
analyse = function_from("q09", "analyse")

assert calculate(8, "/", 2) == 4
assert is_prime(29) and not is_prime(1) and not is_prime(35)
assert is_palindrome("A man, a plan, a canal: Panama")
assert analyse("Hello world!") == {"vowels": 3, "consonants": 7, "words": 2}
print("Algorithm checks passed.")
