# token.py: Defines token types and the Token class for the calculator lexer
from enum import Enum, auto
from dataclasses import dataclass

# TokenType: Enumerates all possible token types
class TokenType(Enum):
    NUMBER = auto()   # Numeric literal
    IDENT = auto()    # Identifier (variable or function name)
    PLUS = auto()     # '+'
    MINUS = auto()    # '-'
    STAR = auto()     # '*'
    SLASH = auto()    # '/'
    CARET = auto()    # '^'
    LPAREN = auto()   # '('
    RPAREN = auto()   # ')'
    COMMA = auto()    # ','
    ASSIGN = auto()   # '='
    NEWLINE = auto()  # Newline
    EOF = auto()      # End of file/input

# Token: Represents a single token from the input
@dataclass(frozen=True)
class Token:
    type: TokenType   # The type of token
    lexeme: str       # The string value of the token
    value: float | None  # The numeric value (if applicable)
    line: int         # Line number in the input
    col: int          # Column number in the input
