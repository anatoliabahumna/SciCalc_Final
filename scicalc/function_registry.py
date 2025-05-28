
import math
class FunctionRegistry:
    def __init__(self):
        self.f={k:getattr(math,k) for k in ['sin','cos','tan','sqrt','log','exp','ceil','floor','fabs']}
        self.f['root']=lambda x,n: math.pow(x,1/n)
        self.f['pow']=math.pow
        self.f['abs']=abs
    def add(self,k,f): self.f[k]=f
    def call(self,n,args):
        if n not in self.f: raise KeyError(n)
        return self.f[n](*args)
