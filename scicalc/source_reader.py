# SourceReader: Utility to read characters from input text with line/column tracking
class SourceReader:
    def __init__(self, text:str):
        # t: input text, i: index, l: unused, c: unused
        self.t=text
        self.i=self.l=self.c=0
        self.line=1  # Current line number
        self.col=1   # Current column number
    def peek(self,o=0):
        # Peek at the character at offset o from current position
        j=self.i+o
        return self.t[j] if j<len(self.t) else ''
    def next(self):
        # Advance to the next character and update line/col
        ch=self.peek()
        if ch:
            self.i+=1
            if ch=='\n':
                self.line+=1
                self.col=1
            else:
                self.col+=1
        return ch
    def eof(self): return self.i>=len(self.t)  # Check if end of file
