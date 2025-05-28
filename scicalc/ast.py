
from dataclasses import dataclass
@dataclass(frozen=True)
class Num: v:float
@dataclass(frozen=True)
class Var: n:str
@dataclass(frozen=True)
class Unary: op:str; e:object
@dataclass(frozen=True)
class Bin: op:str; l:object; r:object
@dataclass(frozen=True)
class Assign: n:str; e:object
@dataclass(frozen=True)
class Call: n:str; a:tuple
