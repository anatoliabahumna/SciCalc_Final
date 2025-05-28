# scanner.py: Tokenizes input text for the calculator
from .token import Token, TokenType as T
from .source_reader import SourceReader
from .errors import LexerError

def scan(text:str):
    """Generator that yields tokens from the input text."""
    r=SourceReader(text)
    while not r.eof():
        ch=r.peek()
        # Skip whitespace
        if ch in ' \t\r':
            r.next(); continue
        # Handle newlines
        if ch=='\n':
            r.next(); yield Token(T.NEWLINE,'\n',None,r.line,r.col); continue
        # Handle numbers (integers and decimals)
        if ch.isdigit() or (ch=='.' and r.peek(1).isdigit()):
            yield _num(r); continue
        # Handle identifiers (variables/functions)
        if ch.isalpha():
            yield _ident(r); continue
        # Handle operators and punctuation
        m={'+':T.PLUS,'-':T.MINUS,'*':T.STAR,'/':T.SLASH,'^':T.CARET,
           '(':T.LPAREN,')':T.RPAREN,',':T.COMMA,'=':T.ASSIGN}.get(ch)
        if m:
            yield Token(m,r.next(),None,r.line,r.col); continue
        # Raise error for unknown character
        raise LexerError(f'bad char {ch!r} at {r.line}:{r.col}')
    yield Token(T.EOF,'',None,r.line,r.col)

def _num(r):
    """Parse a number token from the input."""
    start_line,start_col=r.line,r.col
    lex=''
    dot=False
    while True:
        ch=r.peek()
        if not ch: break
        if ch=='.':
            if dot: break
            dot=True
            lex+=r.next(); continue
        if ch.isdigit():
            lex+=r.next(); continue
        break
    return Token(T.NUMBER,lex,float(lex),start_line,start_col)

def _ident(r):
    """Parse an identifier token from the input."""
    start_line,start_col=r.line,r.col
    lex=''
    while True:
        ch=r.peek()
        if ch.isalnum() or ch=='_':
            lex+=r.next()
        else:
            break
    return Token(T.IDENT,lex,None,start_line,start_col)
