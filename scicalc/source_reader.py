
class SourceReader:
    def __init__(self, text:str):
        self.t=text
        self.i=self.l=self.c=0
        self.line=1
        self.col=1
    def peek(self,o=0):
        j=self.i+o
        return self.t[j] if j<len(self.t) else ''
    def next(self):
        ch=self.peek()
        if ch:
            self.i+=1
            if ch=='\n':
                self.line+=1
                self.col=1
            else:
                self.col+=1
        return ch
    def eof(self): return self.i>=len(self.t)
