# Evaluator class: Evaluates AST nodes for the calculator
import math
from .ast import Num,Var,Unary,Bin,Assign,Call
from .function_registry import FunctionRegistry
from .errors import EvaluationError

class Evaluator:
    def __init__(self):
        # Stores variable values
        self.vars={}
        # Handles function calls
        self.funcs=FunctionRegistry()
    def eval(self,node):
        # Evaluate a number node
        if isinstance(node,Num): return node.v
        # Evaluate a variable node
        if isinstance(node,Var):
            if node.n not in self.vars: raise EvaluationError('undef var')
            return self.vars[node.n]
        # Evaluate a unary operation node
        if isinstance(node,Unary):
            v=self.eval(node.e)
            return v if node.op=='+' else -v
        # Evaluate a binary operation node
        if isinstance(node,Bin):
            l=self.eval(node.l); r=self.eval(node.r)
            if node.op=='+': return l+r
            if node.op=='-': return l-r
            if node.op=='*': return l*r
            if node.op=='/':
                if r==0: raise EvaluationError('div0')
                return l/r
            if node.op=='^': return math.pow(l,r)
        # Evaluate an assignment node
        if isinstance(node,Assign):
            v=self.eval(node.e); self.vars[node.n]=v; return v
        # Evaluate a function call node
        if isinstance(node,Call):
            a=[self.eval(x) for x in node.a]
            return self.funcs.call(node.n,a)
        # Raise error for unknown node
        raise EvaluationError('bad node')
