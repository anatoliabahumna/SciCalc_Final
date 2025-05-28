
from .token import TokenType as T
from .scanner import scan
from .ast import Num,Var,Unary,Bin,Assign,Call
from .errors import ParserError

class Parser:
    def __init__(self,txt:str):
        self.t=list(scan(txt))
        self.p=0
    def parse(self):
        res=[]
        while not self._check(T.EOF):
            if self._check(T.NEWLINE):
                self._adv(); continue
            res.append(self._stmt())
            self._eat(T.NEWLINE,'newline')
        return res
    def _stmt(self):
        if self._check(T.IDENT) and self._peek(1).type==T.ASSIGN:
            name=self._adv().lexeme
            self._adv()
            return Assign(name,self._expr())
        return self._expr()
    def _expr(self):
        node=self._term()
        while self._match(T.PLUS,T.MINUS):
            op=self._prev().lexeme
            node=Bin(op,node,self._term())
        return node
    def _term(self):
        node=self._pow()
        while self._match(T.STAR,T.SLASH):
            op=self._prev().lexeme
            node=Bin(op,node,self._pow())
        return node
    def _pow(self):
        node=self._unary()
        if self._match(T.CARET):
            op='^'
            node=Bin(op,node,self._pow())
        return node
    def _unary(self):
        if self._match(T.PLUS,T.MINUS):
            return Unary(self._prev().lexeme,self._unary())
        return self._prim()
    def _prim(self):
        if self._match(T.NUMBER):
            return Num(self._prev().value)
        if self._match(T.IDENT):
            name=self._prev().lexeme
            if self._match(T.LPAREN):
                args=[]
                if not self._check(T.RPAREN):
                    args.append(self._expr())
                    while self._match(T.COMMA):
                        args.append(self._expr())
                self._eat(T.RPAREN,')')
                return Call(name,tuple(args))
            return Var(name)
        if self._match(T.LPAREN):
            e=self._expr()
            self._eat(T.RPAREN,')')
            return e
        raise ParserError('syntax error')
    # helpers
    def _match(self,*k):
        for t in k:
            if self._check(t):
                self._adv(); return True
        return False
    def _eat(self,t,msg):
        if self._check(t): return self._adv()
        raise ParserError(f'expect {msg}')
    def _check(self,t): return self.t[self.p].type==t
    def _peek(self,o): return self.t[self.p+o]
    def _adv(self): self.p+=1; return self.t[self.p-1]
    def _prev(self): return self.t[self.p-1]
