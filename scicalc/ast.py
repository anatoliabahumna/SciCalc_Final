# ast.py: Defines AST node classes for the calculator
from dataclasses import dataclass

# Num: Numeric literal node
@dataclass(frozen=True)
class Num: v:float
# Var: Variable node
@dataclass(frozen=True)
class Var: n:str
# Unary: Unary operation node (e.g., -x)
@dataclass(frozen=True)
class Unary: op:str; e:object
# Bin: Binary operation node (e.g., x + y)
@dataclass(frozen=True)
class Bin: op:str; l:object; r:object
# Assign: Assignment node (e.g., x = 2)
@dataclass(frozen=True)
class Assign: n:str; e:object
# Call: Function call node (e.g., sin(x))
@dataclass(frozen=True)
class Call: n:str; a:tuple
