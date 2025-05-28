# main.py: Entry point and CLI for the scientific calculator
import argparse, sys
from .parser import Parser
from .evaluator import Evaluator
from .errors import CalculatorError

def _fmt(val, precision):
    """Format numeric values with specified precision."""
    if isinstance(val, (int, float)) and precision is not None:
        return f"{val:.{precision}f}"
    return str(val)

def run(text: str, precision: int | None = None) -> list[str]:
    """Run calculator on input text line by line and return results as a list."""
    ev = Evaluator()                 # one evaluator for all lines
    results = []

    for lineno, line in enumerate(text.splitlines(), start=1):
        if not line.strip():         # skip completely blank lines
            continue
        try:
            ast = Parser(line + "\n").parse()[0]   # parse just that line
            value = ev.eval(ast)     # using eval() as that's the method name in our code
            results.append(_fmt(value, precision))
        except CalculatorError as err:
            results.append(f"ERROR line {lineno}: {err}")

    return results

def cli():
    """Command-line interface for the calculator."""
    p=argparse.ArgumentParser()
    p.add_argument('-i','--input')
    p.add_argument('-o','--output')
    p.add_argument('--precision', type=int, help='Number of decimal places for output')
    a=p.parse_args()
    # Read input from file or stdin
    txt=open(a.input).read() if a.input else sys.stdin.read()
    res=run(txt, a.precision)
    out='\n'.join(res)
    # Write output to file or stdout
    if a.output:
        open(a.output,'w').write(out)
    else:
        print(out)

if __name__=='__main__': cli()
