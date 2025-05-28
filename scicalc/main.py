# main.py: Entry point and CLI for the scientific calculator
import argparse, sys
from .parser import Parser
from .evaluator import Evaluator
from .errors import CalculatorError

def run(txt:str,ev=None):
    """Run calculator on input text and return results as a list."""
    ev=ev or Evaluator()
    out=[]
    try:
        nodes=Parser(txt).parse()
    except CalculatorError as e:
        return [f'ERROR {e}']
    for n in nodes:
        try:
            out.append(ev.eval(n))
        except CalculatorError as e:
            out.append(f'ERROR {e}')
    return out

def cli():
    """Command-line interface for the calculator."""
    p=argparse.ArgumentParser()
    p.add_argument('-i','--input')
    p.add_argument('-o','--output')
    a=p.parse_args()
    # Read input from file or stdin
    txt=open(a.input).read() if a.input else sys.stdin.read()
    res=run(txt)
    out='\n'.join(map(str,res))
    # Write output to file or stdout
    if a.output:
        open(a.output,'w').write(out)
    else:
        print(out)

if __name__=='__main__': cli()
